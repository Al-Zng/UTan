import SwiftUI

struct NetflixPulseLoader: View {
    @State private var isAnimating = false
    var body: some View {
        VStack(spacing: 15) {
            ZStack {
                Circle()
                    .stroke(Color(red: 0.89, green: 0.04, blue: 0.08).opacity(0.3), lineWidth: 6)
                    .frame(width: 70, height: 70)
                
                Circle()
                    .trim(from: 0, to: 0.7)
                    .stroke(Color(red: 0.89, green: 0.04, blue: 0.08), lineWidth: 6)
                    .frame(width: 70, height: 70)
                    .rotationEffect(Angle(degrees: isAnimating ? 360 : 0))
                    .animation(Animation.linear(duration: 1).repeatForever(autoreverses: false), value: isAnimating)
            }
            .onAppear { isAnimating = true }
            
            Text("UTAN CINEMA")
                .font(.system(.subheadline, design: .monospaced))
                .font(.system(size: 14, weight: .bold))
                .foregroundColor(.white)
                .opacity(0.8)
        }
    }
}

struct ContentView: View {
    @StateObject private var scraper = MovieScraper()
    @State private var searchText = ""
    @FocusState private var isSearchFocused: Bool
    
    var body: some View {
        NavigationView {
            ZStack {
                Color.black.ignoresSafeArea()
                
                if scraper.isLoading {
                    VStack {
                        Spacer()
                        NetflixPulseLoader()
                        Spacer()
                    }
                } else {
                    ScrollView {
                        VStack(alignment: .leading, spacing: 25) {
                            
                            // Netflix Brand Header
                            HStack {
                                Text("UTAN")
                                    .font(.system(size: 28, weight: .black, design: .rounded))
                                    .foregroundColor(Color(red: 0.89, green: 0.04, blue: 0.08))
                                Spacer()
                                Button(action: { scraper.fetchHome() }) {
                                    Image(systemName: "arrow.clockwise").foregroundColor(.white)
                                }
                            }
                            .padding(.horizontal)
                            .padding(.top, 12)
                            
                            // Sleek Search Bar
                            HStack {
                                Image(systemName: "magnifyingglass")
                                    .foregroundColor(.gray)
                                TextField("Search movies & series...", text: $searchText)
                                    .foregroundColor(.white)
                                    .submitLabel(.search)
                                    .focused($isSearchFocused)
                                    .onSubmit {
                                        scraper.search(query: searchText)
                                    }
                                if !searchText.isEmpty {
                                    Button(action: { 
                                        searchText = ""
                                        scraper.searchResults = []
                                    }) {
                                        Image(systemName: "xmark.circle.fill").foregroundColor(.gray)
                                    }
                                }
                            }
                            .padding(14)
                            .background(Color(white: 0.12))
                            .cornerRadius(12)
                            .padding(.horizontal)
                            
                            if !searchText.isEmpty || scraper.isSearching {
                                VStack(alignment: .leading, spacing: 15) {
                                    Text("Search Results")
                                        .font(.system(size: 20, weight: .bold))
                                        .foregroundColor(.white)
                                        .padding(.horizontal)
                                    
                                    if scraper.isSearching {
                                        HStack {
                                            Spacer()
                                            ProgressView().tint(.red)
                                            Spacer()
                                        }.padding()
                                    } else if scraper.searchResults.isEmpty {
                                        Text("No titles matched your query.")
                                            .foregroundColor(.gray)
                                            .padding()
                                    } else {
                                        LazyVGrid(columns: [GridItem(.adaptive(minimum: 110), spacing: 15)], spacing: 20) {
                                            ForEach(scraper.searchResults) { item in
                                                NavigationLink(destination: DetailsView(itemId: item.id)) {
                                                    PremiumPosterCard(item: item)
                                                }
                                            }
                                        }
                                        .padding(.horizontal)
                                    }
                                }
                            } else {
                                // Netflix Hero Showcase Banner
                                if !scraper.banners.isEmpty {
                                    TabView {
                                        ForEach(scraper.banners) { hero in
                                            NavigationLink(destination: DetailsView(itemId: hero.id)) {
                                                ZStack(alignment: .bottom) {
                                                    AsyncImage(url: URL(string: hero.imageUrl)) { img in
                                                        img.resizable().aspectRatio(contentMode: .fill)
                                                    } placeholder: {
                                                        Color(white: 0.1)
                                                    }
                                                    .frame(height: 420)
                                                    .clipped()
                                                    
                                                    LinearGradient(colors: [.clear, .black.opacity(0.5), .black], startPoint: .top, endPoint: .bottom)
                                                    
                                                    VStack(spacing: 12) {
                                                        Text(hero.title)
                                                            .font(.system(size: 28, weight: .bold))
                                                            .foregroundColor(.white)
                                                            .multilineTextAlignment(.center)
                                                            .padding(.horizontal)
                                                        
                                                        HStack(spacing: 20) {
                                                            HStack {
                                                                Image(systemName: "play.fill")
                                                                Text("Play Now")
                                                            }
                                                            .font(.system(size: 14, weight: .bold))
                                                            .padding(.horizontal, 24)
                                                            .padding(.vertical, 10)
                                                            .background(Color.white)
                                                            .foregroundColor(.black)
                                                            .cornerRadius(6)
                                                        }
                                                    }
                                                    .padding(.bottom, 45)
                                                }
                                            }
                                        }
                                    }
                                    .frame(height: 420)
                                    .tabViewStyle(PageTabViewStyle())
                                    .cornerRadius(16)
                                    .padding(.horizontal)
                                }
                                
                                // Category Section Headers
                                ForEach(scraper.categoryOrder, id: \.self) { catName in
                                    VStack(alignment: .leading, spacing: 12) {
                                        HStack {
                                            Text(catName)
                                                .font(.system(size: 20, weight: .bold))
                                                .foregroundColor(.white)
                                            Spacer()
                                            NavigationLink(destination: AllCategoryGrid(title: catName, items: scraper.categories[catName] ?? [])) {
                                                Text("View All")
                                                    .font(.system(size: 13, weight: .bold))
                                                    .foregroundColor(Color(red: 0.89, green: 0.04, blue: 0.08))
                                            }
                                        }
                                        .padding(.horizontal)
                                        
                                        ScrollView(.horizontal, showsIndicators: false) {
                                            HStack(spacing: 15) {
                                                ForEach(scraper.categories[catName] ?? [], id: \.self) { item in
                                                    NavigationLink(destination: DetailsView(itemId: item.id)) {
                                                        PremiumPosterCard(item: item)
                                                    }
                                                }
                                            }
                                            .padding(.horizontal)
                                        }
                                    }
                                }
                            }
                        }
                        .padding(.bottom, 40)
                    }
                }
            }
            .navigationBarHidden(true)
        }
        .navigationViewStyle(StackNavigationViewStyle())
        .onAppear {
            if scraper.categories.isEmpty {
                scraper.fetchHome()
            }
        }
    }
}

struct PremiumPosterCard: View {
    let item: VideoItem
    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            AsyncImage(url: URL(string: item.imageUrl)) { image in
                image.resizable().aspectRatio(contentMode: .fill)
            } placeholder: {
                Color(white: 0.1)
            }
            .frame(width: 125, height: 185)
            .clipped()
            .cornerRadius(8)
            .overlay(
                RoundedRectangle(cornerRadius: 8)
                    .stroke(Color.white.opacity(0.1), lineWidth: 0.5)
            )
            
            Text(item.title)
                .font(.system(size: 12, weight: .bold))
                .foregroundColor(.white)
                .lineLimit(2)
                .frame(width: 125, alignment: .leading)
        }
    }
}

struct AllCategoryGrid: View {
    let title: String
    let items: [VideoItem]
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            ScrollView {
                VStack(alignment: .leading, spacing: 20) {
                    Text(title)
                        .font(.system(size: 30, weight: .bold))
                        .foregroundColor(.white)
                        .padding(.horizontal)
                        .padding(.top)
                    
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 110), spacing: 15)], spacing: 20) {
                        ForEach(items) { item in
                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                PremiumPosterCard(item: item)
                            }
                        }
                    }
                    .padding(.horizontal)
                }
            }
        }
        .navigationBarTitleDisplayMode(.inline)
    }
}

struct DetailsView: View {
    let itemId: String
    @StateObject private var scraper = MovieScraper()
    @State private var details: MediaDetails?
    @State private var loadingDetails = true
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            if loadingDetails {
                NetflixPulseLoader()
            } else if let details = details {
                ScrollView {
                    VStack(alignment: .leading, spacing: 18) {
                        ZStack(alignment: .bottomLeading) {
                            AsyncImage(url: URL(string: details.imageUrl)) { image in
                                image.resizable().aspectRatio(contentMode: .fill)
                            } placeholder: {
                                Color(white: 0.1)
                            }
                            .frame(height: 350)
                            .clipped()
                            
                            LinearGradient(colors: [.clear, .black.opacity(0.8), .black], startPoint: .top, endPoint: .bottom)
                            
                            VStack(alignment: .leading, spacing: 12) {
                                Text(details.title)
                                    .font(.system(size: 28, weight: .bold))
                                    .foregroundColor(.white)
                                
                                HStack(spacing: 15) {
                                    if !details.year.isEmpty {
                                        Text(details.year)
                                            .font(.system(size: 14, weight: .bold))
                                            .foregroundColor(.white.opacity(0.7))
                                    }
                                    
                                    if !details.rating.isEmpty {
                                        HStack(spacing: 4) {
                                            Image(systemName: "star.fill").foregroundColor(.yellow)
                                            Text(details.rating).foregroundColor(.white)
                                        }
                                        .font(.system(size: 14, weight: .bold))
                                    }
                                    
                                    if !details.runtime.isEmpty {
                                        Text(details.runtime)
                                            .font(.system(size: 14))
                                            .foregroundColor(.white.opacity(0.7))
                                    }
                                }
                            }
                            .padding()
                        }
                        
                        VStack(alignment: .leading, spacing: 15) {
                            if details.isMovie {
                                NavigationLink(destination: CustomPlayerView(
                                    videoUrl: details.movieUrl,
                                    videoUrl1080: details.movieUrl1080,
                                    videoUrl360: details.movieUrl360,
                                    subtitleUrl: details.movieSubtitleUrl,
                                    webvttUrl: details.movieWebvttUrl
                                )) {
                                    HStack {
                                        Image(systemName: "play.fill")
                                        Text("Watch Movie Now")
                                            .font(.system(size: 16, weight: .bold))
                                    }
                                    .frame(maxWidth: .infinity)
                                    .padding()
                                    .background(Color(red: 0.89, green: 0.04, blue: 0.08))
                                    .foregroundColor(.white)
                                    .cornerRadius(8)
                                }
                            }
                            
                            Text("Synopsis")
                                .font(.headline)
                                .foregroundColor(.white)
                            
                            Text(details.synopsis.isEmpty ? "No description available for this title." : details.synopsis)
                                .font(.body)
                                .foregroundColor(.white.opacity(0.8))
                                .lineSpacing(4)
                            
                            if !details.genre.isEmpty {
                                Text("Genre: \(details.genre)")
                                    .font(.caption)
                                    .foregroundColor(.gray)
                            }
                        }
                        .padding(.horizontal)
                        
                        if !details.isMovie {
                            VStack(alignment: .leading, spacing: 15) {
                                Text("Episodes")
                                    .font(.headline)
                                    .foregroundColor(.white)
                                    .padding(.horizontal)
                                
                                LazyVStack(spacing: 10) {
                                    ForEach(details.episodes) { episode in
                                        NavigationLink(destination: CustomPlayerView(
                                            videoUrl: episode.url,
                                            videoUrl1080: episode.url1080,
                                            videoUrl360: episode.url360,
                                            subtitleUrl: episode.subtitleUrl,
                                            webvttUrl: episode.webvttUrl
                                        )) {
                                            HStack {
                                                VStack(alignment: .leading, spacing: 4) {
                                                    Text(episode.title)
                                                        .foregroundColor(.white)
                                                        .font(.system(size: 15, weight: .semibold))
                                                    Text("Quality: 1080p, 360p Available")
                                                        .font(.system(size: 12))
                                                        .foregroundColor(.gray)
                                                }
                                                Spacer()
                                                Image(systemName: "play.circle.fill")
                                                    .foregroundColor(.white.opacity(0.5))
                                                    .font(.title2)
                                            }
                                            .padding()
                                            .background(Color(white: 0.15))
                                            .cornerRadius(10)
                                        }
                                    }
                                }
                                .padding(.horizontal)
                            }
                        }
                    }
                    .padding(.bottom, 40)
                }
            }
        }
        .onAppear {
            scraper.fetchDetails(id: itemId) { result in
                self.details = result
                self.loadingDetails = false
            }
        }
    }
}
