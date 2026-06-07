import SwiftUI

let UT_RED = Color(red: 0.85, green: 0.1, blue: 0.1)

struct MainTabView: View {
    @StateObject var scraper = UTScraper()
    @StateObject var store = UTStore()
    
    var body: some View {
        TabView {
            HomeView().tabItem { Label("الرئيسية", systemImage: "house.fill") }
            BrowseView().tabItem { Label("تصفح", systemImage: "square.grid.2x2.fill") }
            SearchView().tabItem { Label("بحث", systemImage: "magnifyingglass") }
            HistoryView().tabItem { Label("السجل", systemImage: "clock.fill") }
        }
        .accentColor(UT_RED)
        .environmentObject(scraper)
        .environmentObject(store)
    }
}

struct HomeView: View {
    @EnvironmentObject var scraper: UTScraper
    var body: some View {
        NavigationView {
            ScrollView {
                LazyVGrid(columns: [GridItem(.flexible()), GridItem(.flexible())], spacing: 15) {
                    ForEach(scraper.homeItems) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            VStack(alignment: .leading) {
                                AsyncImage(url: URL(string: item.imageUrl)) { img in
                                    img.resizable().aspectRatio(2/3, contentMode: .fill)
                                } placeholder: { Color.gray }
                                .cornerRadius(8)
                                Text(item.title).font(.caption).bold().lineLimit(1).foregroundColor(.white)
                            }
                        }
                    }
                }.padding()
            }
            .navigationTitle("UTan")
            .onAppear { scraper.fetchHome() }
        }
    }
}

struct DetailsView: View {
    let itemId: String
    @EnvironmentObject var scraper: UTScraper
    @EnvironmentObject var store: UTStore
    @State private var details: MediaDetails?
    @State private var selectedEpisode: EpisodeItem?
    
    var body: some View {
        ScrollView {
            if let d = details {
                VStack(alignment: .leading) {
                    AsyncImage(url: URL(string: d.imageUrl)).frame(height: 300).clipped()
                    VStack(alignment: .leading, spacing: 10) {
                        Text(d.title).font(.title).bold()
                        Text(d.desc).font(.body).foregroundColor(.gray)
                        
                        Text("الحلقات").font(.headline).padding(.top)
                        ForEach(d.episodes) { ep in
                            Button(ep.title) { selectedEpisode = ep }
                                .padding().frame(maxWidth: .infinity).background(Color.gray.opacity(0.2)).cornerRadius(8)
                        }
                    }.padding()
                }
            }
        }
        .onAppear { scraper.fetchDetails(id: itemId) { details = $0 } }
        .fullScreenCover(item: $selectedEpisode) { ep in
            if let url = URL(string: ep.url) { CustomPlayer(url: url) }
        }
    }
}

struct BrowseView: View { var body: some View { Text("Browse") } }
struct SearchView: View { var body: some View { Text("Search") } }
struct HistoryView: View { var body: some View { Text("History") } }


