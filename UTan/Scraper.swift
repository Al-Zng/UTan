import Foundation

// MARK: – Data Models

struct VideoItem: Identifiable, Hashable, Codable {
    let id: String
    let title: String
    let imageUrl: String
    let type: String
}

struct EpisodeItem: Identifiable, Hashable {
    let id: String
    let title: String
    let url: String
    let url1080: String
    let url360: String
    let subtitleUrl: String
    let subtitleVttUrl: String
}

struct MediaDetails {
    let title: String
    let imageUrl: String
    let type: String
    let desc: String
    let episodes: [EpisodeItem]
}

struct WatchProgress: Codable {
    let itemId: String
    let episodeId: String
    let progressSeconds: Double
    let durationSeconds: Double
    let lastUpdated: Date
}

class UTStore: ObservableObject {
    @Published var history: [VideoItem] = []
    @Published var progress: [String: WatchProgress] = [:]
    
    private let histKey = "ut_history"
    private let progKey = "ut_progress"
    
    init() {
        load()
    }
    
    func addToHistory(_ item: VideoItem) {
        if let idx = history.firstIndex(where: { $0.id == item.id }) {
            history.remove(at: idx)
        }
        history.insert(item, at: 0)
        if history.count > 50 { history.removeLast() }
        save()
    }
    
    func updateProgress(itemId: String, epId: String, current: Double, total: Double) {
        let p = WatchProgress(itemId: itemId, episodeId: epId, progressSeconds: current, durationSeconds: total, lastUpdated: Date())
        progress[itemId] = p
        save()
    }
    
    func progress(for itemId: String) -> WatchProgress? {
        progress[itemId]
    }
    
    private func save() {
        if let d = try? JSONEncoder().encode(history) { UserDefaults.standard.set(d, forKey: histKey) }
        if let d = try? JSONEncoder().encode(progress) { UserDefaults.standard.set(d, forKey: progKey) }
    }
    
    private func load() {
        if let d = UserDefaults.standard.data(forKey: histKey), let h = try? JSONDecoder().decode([VideoItem].self, from: d) { history = h }
        if let d = UserDefaults.standard.data(forKey: progKey), let p = try? JSONDecoder().decode([String: WatchProgress].self, from: d) { progress = p }
    }
}

class UTScraper: ObservableObject {
    @Published var homeItems: [VideoItem] = []
    @Published var browseItems: [VideoItem] = []
    @Published var searchResults: [VideoItem] = []
    @Published var isLoading = false
    
    private let baseUrl = "https://utan.me"
    
    func fetchHome() {
        isLoading = true
        // Mock fetch logic
        DispatchQueue.main.asyncAfter(deadline: .now() + 1) {
            self.homeItems = (1...12).map { VideoItem(id: "\($0)", title: "فيلم/مسلسل تجريبي \($0)", imageUrl: "https://picsum.photos/400/600?random=\($0)", type: "Movie") }
            self.isLoading = false
        }
    }
    
    func fetchDetails(id: String, completion: @escaping (MediaDetails?) -> Void) {
        // Mock detail fetch
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
            let eps = (1...24).map { EpisodeItem(id: "ep\($0)", title: "الحلقة \($0)", url: "https://test-streams.mux.dev/x36xhzz/x36xhzz.m3u8", url1080: "", url360: "", subtitleUrl: "", subtitleVttUrl: "") }
            let d = MediaDetails(title: "عنوان العمل", imageUrl: "https://picsum.photos/400/600", type: "Series", desc: "هذا نص تجريبي لوصف العمل المختار. يتم جلب البيانات الحقيقية من الموقع مباشرة عبر الكاشط.", episodes: eps)
            completion(d)
        }
    }
}
