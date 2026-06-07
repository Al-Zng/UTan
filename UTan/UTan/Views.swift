import SwiftUI

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Loader
// ─────────────────────────────────────────────────────────────────────────────
struct UTanLoader: View {
    @State private var spin = false
    var body: some View {
        VStack(spacing: 20) {
            ZStack {
                Image("app") // app.png from Assets
                    .resizable()
                    .scaledToFit()
                    .frame(width: 100, height: 100)
                    .cornerRadius(20)
                
                Circle()
                    .trim(from: 0, to: 0.72)
                    .stroke(UT_RED, style: StrokeStyle(lineWidth: 4, lineCap: .round))
                    .frame(width: 120, height: 120)
                    .rotationEffect(.degrees(spin ? 360 : 0))
                    .animation(.linear(duration: 1.5).repeatForever(autoreverses: false), value: spin)
            }
            .onAppear { spin = true }
            
            Text("UTAN")
                .font(.system(size: 18, weight: .bold, design: .rounded))
                .foregroundColor(.white)
                .tracking(4)
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Player Presentation Data Structure
// ─────────────────────────────────────────────────────────────────────────────
struct PlayerData: Identifiable {
    let id = UUID()
    let itemId: String
    let itemTitle: String
    let itemImageUrl: String
    let videoUrl: String
    let videoUrl1080: String
    let videoUrl360: String
    let subtitleUrl: String
    let subtitleVttUrl: String
    let episodeId: String
    let episodeTitle: String
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Poster card
// ─────────────────────────────────────────────────────────────────────────────
struct PosterCard: View {
    let item: VideoItem
    var progress: WatchProgress? = nil

    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            ZStack(alignment: .bottom) {
                AsyncImage(url: URL(string: item.imageUrl)) { img in
                    img.resizable().aspectRatio(contentMode: .fill)
                } placeholder: {
                    Color(white: 0.12)
                }
                .frame(width: 120, height: 180)
                .clipped()
                .cornerRadius(16)
                
                // Overlay Gradient
                LinearGradient(colors: [.clear, .black.opacity(0.8)], startPoint: .center, endPoint: .bottom)
                    .cornerRadius(16)

                if let p = progress, p.durationSeconds > 0 {
                    GeometryReader { geo in
                        ZStack(alignment: .leading) {
                            Color.white.opacity(0.3).frame(height: 4)
                            UT_RED.frame(width: geo.size.width * min(1, CGFloat(p.progressSeconds / p.durationSeconds)), height: 4)
                        }
                    }
                    .frame(height: 4)
                    .padding(.horizontal, 8)
                    .padding(.bottom, 8)
                }
            }
            .frame(width: 120, height: 180)
            .shadow(color: .black.opacity(0.4), radius: 5, x: 0, y: 4)

            Text(item.title)
                .font(.system(size: 12, weight: .bold))
                .foregroundColor(.white)
                .lineLimit(2)
                .frame(width: 120, alignment: .leading)
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – MainTabView
// ─────────────────────────────────────────────────────────────────────────────
struct MainTabView: View {
    @StateObject private var scraper = MovieScraper()

    var body: some View {
        TabView {
            HomeView(scraper: scraper)
                .tabItem { Label("الرئيسية", systemImage: "house.fill") }
            BrowseView(scraper: scraper)
                .tabItem { Label("تصفح", systemImage: "square.grid.2x2.fill") }
            SearchView(scraper: scraper)
                .tabItem { Label("بحث", systemImage: "magnifyingglass") }
            DownloadsView()
                .tabItem { Label("التحميلات", systemImage: "arrow.down.circle.fill") }
            SettingsView()
                .tabItem { Label("المزيد", systemImage: "line.3.horizontal") }
        }
        .accentColor(UT_RED)
        .preferredColorScheme(.dark)
        .onAppear {
            let appearance = UITabBarAppearance()
            appearance.configureWithOpaqueBackground()
            appearance.backgroundColor = UIColor(APP_BG)
            UITabBar.appearance().standardAppearance = appearance
            if #available(iOS 15.0, *) {
                UITabBar.appearance().scrollEdgeAppearance = appearance
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – HomeView (Full-Screen Hero + Overlapping Cards)
// ─────────────────────────────────────────────────────────────────────────────
struct HomeView: View {
    @ObservedObject var scraper: MovieScraper
    @ObservedObject private var progressStore = WatchProgressStore.shared
    
    @State private var playItem: PlayerData?

    var body: some View {
        NavigationView {
            ZStack(alignment: .top) {
                APP_BG.ignoresSafeArea()
                
                if scraper.isLoading {
                    UTanLoader().frame(maxHeight: .infinity)
                } else {
                    ScrollView(showsIndicators: false) {
                        VStack(spacing: 0) {
                            if !scraper.heroItems.isEmpty {
                                HeroBanner(items: scraper.heroItems, scraper: scraper)
                                    .frame(height: UIScreen.main.bounds.height * 0.75)
                            }

                            VStack(alignment: .leading, spacing: 30) {
                                if !progressStore.recent.isEmpty {
                                    ContinueWatchingRow(items: progressStore.recent, playItem: $playItem)
                                        .padding(.top, -60) // Overlap the hero section
                                        .zIndex(1)
                                }

                                ForEach(scraper.categories, id: \.name) { cat in
                                    if !cat.items.isEmpty {
                                        CategoryRow(title: cat.name, items: cat.items)
                                    }
                                }
                            }
                            .padding(.bottom, 100)
                        }
                    }
                    .ignoresSafeArea(.all, edges: .top)
                }
                
                // Floating Brand
                HStack {
                    Image("logo") // logo.png from Assets
                        .resizable()
                        .scaledToFit()
                        .frame(height: 40)
                    Spacer()
                }
                .padding(.horizontal, 20)
                .padding(.top, 50)
            }
            .navigationBarHidden(true)
            .fullScreenCover(item: $playItem) { data in
                CustomPlayerView(
                    itemId: data.itemId, itemTitle: data.itemTitle, itemImageUrl: data.itemImageUrl,
                    videoUrl: data.videoUrl, videoUrl1080: data.videoUrl1080, videoUrl360: data.videoUrl360,
                    subtitleUrl: data.subtitleUrl, subtitleVttUrl: data.subtitleVttUrl,
                    episodeId: data.episodeId, episodeTitle: data.episodeTitle
                )
            }
        }
        .navigationViewStyle(StackNavigationViewStyle())
        .onAppear { if scraper.heroItems.isEmpty { scraper.fetchHome() } }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Hero Banner
// ─────────────────────────────────────────────────────────────────────────────
struct HeroBanner: View {
    let items: [VideoItem]
    @ObservedObject var scraper: MovieScraper
    @State private var current = 0
    @State private var timer: Timer?
    @ObservedObject var favStore = FavoritesStore.shared

    var body: some View {
        TabView(selection: $current) {
            ForEach(items.prefix(8).indices, id: \.self) { i in
                let item = items[i]
                ZStack(alignment: .bottom) {
                    AsyncImage(url: URL(string: item.imageUrl)) { img in
                        img.resizable().aspectRatio(contentMode: .fill)
                    } placeholder: { Color(white: 0.05) }
                    .frame(maxWidth: .infinity, maxHeight: .infinity)
                    .clipped()

                    LinearGradient(colors: [.clear, APP_BG.opacity(0.8), APP_BG],
                                   startPoint: .center, endPoint: .bottom)
                    
                    VStack(spacing: 16) {
                        Text(item.title)
                            .font(.system(size: 32, weight: .heavy))
                            .foregroundColor(.white)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal)
                            .shadow(color: .black, radius: 4)

                        HStack(spacing: 20) {
                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                HStack {
                                    Image(systemName: "play.fill")
                                    Text("شاهد الآن")
                                }
                                .font(.system(size: 16, weight: .bold))
                                .padding(.horizontal, 30).padding(.vertical, 12)
                                .background(UT_RED)
                                .foregroundColor(.white)
                                .cornerRadius(12)
                            }
                            
                            Button {
                                favStore.toggle(item: item)
                            } label: {
                                VStack(spacing: 6) {
                                    Image(systemName: favStore.isFavorite(item.id) ? "checkmark" : "plus")
                                        .font(.system(size: 20, weight: .bold))
                                    Text("قائمتي").font(.system(size: 10, weight: .semibold))
                                }
                                .foregroundColor(.white)
                            }
                        }
                        .padding(.bottom, 80)
                    }
                }
                .tag(i)
            }
        }
        .tabViewStyle(.page(indexDisplayMode: .never))
        .onAppear { startTimer() }
        .onDisappear { timer?.invalidate() }
    }

    private func startTimer() {
        timer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            withAnimation(.easeInOut(duration: 0.8)) { current = (current + 1) % min(items.count, 8) }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Continue Watching Row (Direct Play)
// ─────────────────────────────────────────────────────────────────────────────
struct ContinueWatchingRow: View {
    let items: [WatchProgress]
    @Binding var playItem: PlayerData?

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text("متابعة المشاهدة")
                .font(.system(size: 20, weight: .bold)).foregroundColor(.white)
                .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 16) {
                    ForEach(items.prefix(10)) { prog in
                        Button {
                            playItem = PlayerData(
                                itemId: prog.itemId, itemTitle: prog.title, itemImageUrl: prog.imageUrl,
                                videoUrl: prog.videoUrl, videoUrl1080: prog.videoUrl1080, videoUrl360: prog.videoUrl360,
                                subtitleUrl: prog.subtitleUrl, subtitleVttUrl: prog.subtitleVttUrl,
                                episodeId: prog.episodeId, episodeTitle: prog.episodeTitle
                            )
                        } label: {
                            VStack(alignment: .leading, spacing: 8) {
                                ZStack(alignment: .center) {
                                    AsyncImage(url: URL(string: prog.imageUrl)) { img in
                                        img.resizable().aspectRatio(contentMode: .fill)
                                    } placeholder: { Color(white: 0.12) }
                                    .frame(width: 160, height: 100)
                                    .clipped()
                                    .cornerRadius(12)
                                    
                                    Color.black.opacity(0.3).cornerRadius(12)
                                    
                                    Image(systemName: "play.circle.fill")
                                        .font(.system(size: 40))
                                        .foregroundColor(.white.opacity(0.9))

                                    if prog.durationSeconds > 0 {
                                        VStack {
                                            Spacer()
                                            GeometryReader { geo in
                                                ZStack(alignment: .leading) {
                                                    Color.white.opacity(0.3).frame(height: 4)
                                                    UT_RED.frame(
                                                        width: geo.size.width * CGFloat(min(1, prog.progressSeconds / prog.durationSeconds)),
                                                        height: 4)
                                                }
                                            }
                                            .frame(height: 4)
                                        }
                                        .padding(.horizontal, 4).padding(.bottom, 4)
                                    }
                                }
                                .frame(width: 160, height: 100)

                                Text(prog.title)
                                    .font(.system(size: 13, weight: .bold))
                                    .foregroundColor(.white).lineLimit(1)
                                    .frame(width: 160, alignment: .leading)

                                if !prog.episodeTitle.isEmpty {
                                    Text(prog.episodeTitle)
                                        .font(.system(size: 11, weight: .medium))
                                        .foregroundColor(.gray).lineLimit(1)
                                        .frame(width: 160, alignment: .leading)
                                }
                            }
                        }
                    }
                }
                .padding(.horizontal)
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Category Row
// ─────────────────────────────────────────────────────────────────────────────
struct CategoryRow: View {
    let title: String
    let items: [VideoItem]
    @ObservedObject private var store = WatchProgressStore.shared

    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            Text(title)
                .font(.system(size: 20, weight: .bold)).foregroundColor(.white)
                .padding(.horizontal)

            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 14) {
                    ForEach(items) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item, progress: store.progress(for: item.id))
                        }
                    }
                }
                .padding(.horizontal)
            }
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Browse & Category Lists
// ─────────────────────────────────────────────────────────────────────────────
struct BrowseView: View {
    @ObservedObject var scraper: MovieScraper
    let cols = [GridItem(.flexible()), GridItem(.flexible())]

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                ScrollView {
                    LazyVGrid(columns: cols, spacing: 16) {
                        ForEach(SITE_CATEGORIES) { cat in
                            NavigationLink(destination: CategoryListView(category: cat, scraper: scraper)) {
                                ZStack {
                                    RoundedRectangle(cornerRadius: 16)
                                        .fill(Color.white.opacity(0.05))
                                    VStack(spacing: 8) {
                                        Image(systemName: "film")
                                            .font(.title2)
                                            .foregroundColor(UT_RED)
                                        Text(cat.nameAr)
                                            .font(.system(size: 14, weight: .bold))
                                            .foregroundColor(.white)
                                    }
                                    .padding(10)
                                }
                                .frame(height: 100)
                            }
                        }
                    }
                    .padding()
                }
            }
            .navigationTitle("تصفح")
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }
}

struct CategoryListView: View {
    let category: SiteCategory
    @ObservedObject var scraper: MovieScraper
    @State private var items: [VideoItem] = []
    @State private var page = 1
    @State private var loading = false
    let cols = [GridItem(.adaptive(minimum: 110), spacing: 14)]

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            ScrollView {
                LazyVGrid(columns: cols, spacing: 16) {
                    ForEach(items) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item)
                        }
                        .onAppear { if item.id == items.last?.id { loadMore() } }
                    }
                }
                .padding()
                if loading { UTanLoader().padding() }
            }
        }
        .navigationTitle(category.nameAr)
        .onAppear { if items.isEmpty { loadMore() } }
    }
    private func loadMore() {
        loading = true
        scraper.fetchCategory(typeId: category.id, page: page) { newItems, _ in
            items.append(contentsOf: newItems); page += 1; loading = false
        }
    }
}

struct SearchView: View {
    @ObservedObject var scraper: MovieScraper
    @State private var query = ""
    @State private var results: [VideoItem] = []
    let cols = [GridItem(.adaptive(minimum: 110), spacing: 14)]

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                VStack(spacing: 0) {
                    HStack {
                        Image(systemName: "magnifyingglass").foregroundColor(.gray)
                        TextField("بحث...", text: $query)
                            .foregroundColor(.white)
                            .onSubmit { scraper.search(query: query) { r in results = r } }
                    }
                    .padding(14)
                    .background(Color.white.opacity(0.1))
                    .cornerRadius(12)
                    .padding()

                    ScrollView {
                        LazyVGrid(columns: cols, spacing: 16) {
                            ForEach(results) { item in
                                NavigationLink(destination: DetailsView(itemId: item.id)) { PosterCard(item: item) }
                            }
                        }
                        .padding()
                    }
                }
            }
            .navigationTitle("البحث")
        }
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – Downloads & Settings View
// ─────────────────────────────────────────────────────────────────────────────
struct DownloadsView: View {
    @ObservedObject var manager = DownloadManager.shared
    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                if manager.activeDownloads.isEmpty {
                    VStack(spacing: 20) {
                        Image(systemName: "arrow.down.circle").font(.system(size: 60)).foregroundColor(.gray)
                        Text("لا توجد تحميلات").foregroundColor(.gray)
                    }
                } else {
                    List {
                        ForEach(manager.activeDownloads) { dl in
                            HStack {
                                AsyncImage(url: URL(string: dl.imageUrl)) { img in
                                    img.resizable().aspectRatio(contentMode: .fill)
                                } placeholder: { Color.gray }.frame(width: 50, height: 75).cornerRadius(8)
                                VStack(alignment: .leading) {
                                    Text(dl.title).font(.headline).foregroundColor(.white)
                                    if dl.isCompleted {
                                        Text("مكتمل - محفوظ في الصور").font(.caption).foregroundColor(.green)
                                    } else {
                                        ProgressView(value: dl.progress).tint(UT_RED)
                                        Text("\(Int(dl.progress * 100))%").font(.caption).foregroundColor(.gray)
                                    }
                                }
                                Spacer()
                                Button { manager.cancel(id: dl.id) } label: {
                                    Image(systemName: "xmark.circle.fill").foregroundColor(.red)
                                }
                            }
                            .listRowBackground(Color.white.opacity(0.05))
                        }
                    }
                    .scrollContentBackground(.hidden)
                }
            }
            .navigationTitle("التحميلات")
        }
    }
}

struct SettingsView: View {
    @ObservedObject var settings = AppSettings.shared
    @ObservedObject var historyStore = WatchProgressStore.shared
    @State private var cacheCleared = false

    var body: some View {
        NavigationView {
            ZStack {
                APP_BG.ignoresSafeArea()
                Form {
                    Section(header: Text("إعدادات الترجمة").foregroundColor(UT_RED)) {
                        Toggle("تفعيل الترجمة", isOn: $settings.subtitlesEnabled)
                        if settings.subtitlesEnabled {
                            VStack(alignment: .leading) {
                                Text("حجم الخط: \(Int(settings.subtitleFontSize))")
                                Slider(value: $settings.subtitleFontSize, in: 14...40, step: 1).accentColor(UT_RED)
                            }
                            VStack(alignment: .leading) {
                                Text("الهامش السفلي: \(Int(settings.subtitleBottomPad))")
                                Slider(value: $settings.subtitleBottomPad, in: 20...150, step: 5).accentColor(UT_RED)
                            }
                            VStack(alignment: .leading) {
                                Text("شفافية الخلفية: \(Int(settings.subtitleBgOpacity * 100))%")
                                Slider(value: $settings.subtitleBgOpacity, in: 0.0...1.0, step: 0.1).accentColor(UT_RED)
                            }
                            // Example Colors
                            ScrollView(.horizontal) {
                                HStack {
                                    ForEach(["#FFFFFF", "#FFFF00", "#00FFFF", "#FF00FF"], id: \.self) { hex in
                                        Circle().fill(Color(hex: hex)).frame(width: 30, height: 30)
                                            .overlay(Circle().stroke(Color.white, lineWidth: settings.subtitleColorHex == hex ? 3 : 0))
                                            .onTapGesture { settings.subtitleColorHex = hex }
                                    }
                                }
                            }
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)
                    
                    Section(header: Text("البيانات").foregroundColor(UT_RED)) {
                        NavigationLink(destination: HistoryListView(store: historyStore)) {
                            Text("سجل المشاهدة (\(historyStore.recent.count))")
                        }
                        Button {
                            settings.clearCache()
                            cacheCleared = true
                            DispatchQueue.main.asyncAfter(deadline: .now() + 2) { cacheCleared = false }
                        } label: {
                            Text(cacheCleared ? "تم المسح!" : "مسح التخزين المؤقت والسجل").foregroundColor(.red)
                        }
                    }
                    .listRowBackground(Color.white.opacity(0.05))
                    .foregroundColor(.white)
                }
                .scrollContentBackground(.hidden)
            }
            .navigationTitle("المزيد")
        }
    }
}

struct HistoryListView: View {
    @ObservedObject var store: WatchProgressStore
    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            List {
                ForEach(store.recent) { prog in
                    HStack {
                        AsyncImage(url: URL(string: prog.imageUrl)) { img in img.resizable().aspectRatio(contentMode: .fill) } placeholder: { Color.gray }
                        .frame(width: 50, height: 75).cornerRadius(8)
                        VStack(alignment: .leading) {
                            Text(prog.title).font(.headline).foregroundColor(.white)
                            if !prog.episodeTitle.isEmpty { Text(prog.episodeTitle).font(.caption).foregroundColor(.gray) }
                        }
                    }.listRowBackground(Color.white.opacity(0.05))
                }
                .onDelete { idx in
                    idx.forEach { i in store.remove(itemId: store.recent[i].itemId) }
                }
            }.scrollContentBackground(.hidden)
        }.navigationTitle("سجل المشاهدة")
    }
}

// ─────────────────────────────────────────────────────────────────────────────
// MARK: – DetailsView (Seasons Tabs & Downloads)
// ─────────────────────────────────────────────────────────────────────────────
struct DetailsView: View {
    let itemId: String
    @StateObject private var scraper = MovieScraper()
    @ObservedObject private var favStore = FavoritesStore.shared
    
    @State private var details: MediaDetails?
    @State private var loading = true
    @State private var playerData: PlayerData?
    @State private var selectedSeason: String = ""

    var body: some View {
        ZStack {
            APP_BG.ignoresSafeArea()
            if loading {
                UTanLoader()
            } else if let d = details {
                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 0) {
                        // ── Hero image + overlay
                        ZStack(alignment: .bottomLeading) {
                            AsyncImage(url: URL(string: d.imageUrl)) { img in
                                img.resizable().aspectRatio(contentMode: .fill)
                            } placeholder: { Color(white: 0.1) }
                            .frame(maxWidth: .infinity).frame(height: 350)
                            .clipped()

                            LinearGradient(colors: [.clear, APP_BG.opacity(0.8), APP_BG],
                                           startPoint: .top, endPoint: .bottom)

                            VStack(alignment: .leading, spacing: 12) {
                                Text(d.title)
                                    .font(.system(size: 28, weight: .heavy))
                                    .foregroundColor(.white)

                                HStack(spacing: 10) {
                                    if !d.year.isEmpty { badge(d.year) }
                                    if !d.rating.isEmpty {
                                        HStack(spacing: 3) {
                                            Image(systemName: "star.fill").foregroundColor(.yellow)
                                            Text(d.rating)
                                        }
                                        .font(.system(size: 13, weight: .bold)).foregroundColor(.white)
                                    }
                                    if !d.runtime.isEmpty { badge(d.runtime) }
                                }
                                
                                HStack(spacing: 16) {
                                    if d.isMovie {
                                        Button { playMovie(d: d) } label: {
                                            HStack {
                                                Image(systemName: "play.fill")
                                                Text("شاهد الآن")
                                            }
                                            .font(.system(size: 16, weight: .bold))
                                            .frame(maxWidth: .infinity).padding().background(UT_RED).foregroundColor(.white).cornerRadius(12)
                                        }
                                        
                                        Button {
                                            DownloadManager.shared.startDownload(item: VideoItem(id: itemId, title: d.title, imageUrl: d.imageUrl, type: "post"), isMovie: true, vUrl: d.movieUrl, sUrl: d.movieSubtitleUrl)
                                        } label: { Image(systemName: "arrow.down.circle").font(.title).foregroundColor(.white).padding() }
                                    }
                                    
                                    Button { favStore.toggle(item: VideoItem(id: itemId, title: d.title, imageUrl: d.imageUrl, type: "post")) } label: {
                                        Image(systemName: favStore.isFavorite(itemId) ? "checkmark.circle.fill" : "plus.circle").font(.title).foregroundColor(.white).padding()
                                    }
                                }
                                .padding(.top, 10)
                            }
                            .padding(.horizontal, 20)
                            .padding(.bottom, 20)
                        }

                        // ── Synopsis
                        if !d.synopsis.isEmpty {
                            VStack(alignment: .leading, spacing: 8) {
                                Text("القصة").font(.system(size: 18, weight: .bold)).foregroundColor(.white)
                                Text(d.synopsis).font(.system(size: 15)).foregroundColor(.gray).lineSpacing(6)
                            }
                            .padding(20)
                        }

                        // ── Episodes / Seasons
                        if !d.isMovie && !d.sortedSeasons.isEmpty {
                            VStack(alignment: .leading, spacing: 16) {
                                ScrollView(.horizontal, showsIndicators: false) {
                                    HStack(spacing: 12) {
                                        ForEach(d.sortedSeasons, id: \.self) { season in
                                            Button { selectedSeason = season } label: {
                                                Text(season)
                                                    .font(.system(size: 16, weight: .bold))
                                                    .padding(.horizontal, 20).padding(.vertical, 10)
                                                    .background(selectedSeason == season ? UT_RED : Color.white.opacity(0.1))
                                                    .foregroundColor(selectedSeason == season ? .white : .gray)
                                                    .cornerRadius(12)
                                            }
                                        }
                                    }
                                    .padding(.horizontal, 20)
                                }
                                
                                LazyVStack(spacing: 12) {
                                    let eps = d.seasonsDict[selectedSeason] ?? []
                                    ForEach(eps) { ep in
                                        HStack(spacing: 14) {
                                            Button {
                                                playerData = PlayerData(
                                                    itemId: itemId, itemTitle: d.title, itemImageUrl: d.imageUrl,
                                                    videoUrl: ep.url, videoUrl1080: ep.url1080, videoUrl360: ep.url360,
                                                    subtitleUrl: ep.subtitleUrl, subtitleVttUrl: ep.subtitleVttUrl,
                                                    episodeId: ep.id, episodeTitle: ep.title
                                                )
                                            } label: {
                                                HStack {
                                                    Image(systemName: "play.circle.fill").font(.title2).foregroundColor(UT_RED)
                                                    Text(ep.title).font(.system(size: 14, weight: .bold)).foregroundColor(.white)
                                                    Spacer()
                                                }
                                                .padding()
                                                .background(Color.white.opacity(0.05))
                                                .cornerRadius(12)
                                            }
                                            
                                            Button {
                                                DownloadManager.shared.startDownload(item: VideoItem(id: ep.id, title: ep.title, imageUrl: d.imageUrl, type: "post"), isMovie: false, vUrl: ep.url, sUrl: ep.subtitleUrl)
                                            } label: {
                                                Image(systemName: "arrow.down.circle").foregroundColor(.gray).font(.title3)
                                            }
                                        }
                                        .padding(.horizontal, 20)
                                    }
                                }
                            }
                            .padding(.bottom, 40)
                        }
                    }
                }
            }
        }
        .navigationBarTitleDisplayMode(.inline)
        .fullScreenCover(item: $playerData) { data in
            CustomPlayerView(
                itemId: data.itemId, itemTitle: data.itemTitle, itemImageUrl: data.itemImageUrl,
                videoUrl: data.videoUrl, videoUrl1080: data.videoUrl1080, videoUrl360: data.videoUrl360,
                subtitleUrl: data.subtitleUrl, subtitleVttUrl: data.subtitleVttUrl,
                episodeId: data.episodeId, episodeTitle: data.episodeTitle
            )
        }
        .onAppear {
            scraper.fetchDetails(id: itemId) { result in
                details = result
                if let firstSeason = result.sortedSeasons.first {
                    selectedSeason = firstSeason
                }
                loading = false
            }
        }
    }
    
    private func playMovie(d: MediaDetails) {
        playerData = PlayerData(
            itemId: itemId, itemTitle: d.title, itemImageUrl: d.imageUrl,
            videoUrl: d.movieUrl, videoUrl1080: d.movieUrl1080, videoUrl360: d.movieUrl360,
            subtitleUrl: d.movieSubtitleUrl, subtitleVttUrl: d.movieSubtitleVttUrl,
            episodeId: "", episodeTitle: ""
        )
    }

    private func badge(_ text: String) -> some View {
        Text(text)
            .font(.system(size: 12, weight: .bold))
            .padding(.horizontal, 10).padding(.vertical, 4)
            .background(Color.white.opacity(0.15))
            .cornerRadius(6)
            .foregroundColor(.white)
    }
}
