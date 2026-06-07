import Foundation
import SwiftUI

// ─────────────────────────────────────────────
// MARK: – Global Colors & Configs
// ─────────────────────────────────────────────
let APP_BG = Color(red: 0.05, green: 0.02, blue: 0.09) // Deep Dark Purple / Cinemana Style
let UT_RED = Color(red: 0.89, green: 0.04, blue: 0.08)

class AppSettings: ObservableObject {
    static let shared = AppSettings()
    
    @AppStorage("sub_fontSize") var subtitleFontSize: Double = 22.0
    @AppStorage("sub_colorHex") var subtitleColorHex: String = "#FFFFFF"
    @AppStorage("sub_bgOpacity") var subtitleBgOpacity: Double = 0.6
    @AppStorage("sub_bottomPad") var subtitleBottomPad: Double = 60.0
    @AppStorage("sub_enabled") var subtitlesEnabled: Bool = true
    
    var subtitleColor: Color { Color(hex: subtitleColorHex) }
    
    func clearCache() {
        URLCache.shared.removeAllCachedResponses()
        WatchProgressStore.shared.clearAll()
    }
}

// ─────────────────────────────────────────────
// MARK: – Data Models
// ─────────────────────────────────────────────

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
    
    var season: String {
        let pattern = "(?i)(S\\d+|موسم \\d+)"
        if let rx = try? NSRegularExpression(pattern: pattern),
           let match = rx.firstMatch(in: title, range: NSRange(location: 0, length: title.count)) {
            let nsString = title as NSString
            return nsString.substring(with: match.range).replacingOccurrences(of: "s", with: "S").replacingOccurrences(of: "S", with: "الموسم ")
        }
        return "الموسم 1"
    }
}

struct MediaDetails {
    var title: String = ""
    var imageUrl: String = ""
    var year: String = ""
    var genre: String = ""
    var rating: String = ""
    var runtime: String = ""
    var synopsis: String = ""
    var isMovie: Bool = true
    var movieUrl: String = ""
    var movieUrl1080: String = ""
    var movieUrl360: String = ""
    var movieSubtitleUrl: String = ""
    var movieSubtitleVttUrl: String = ""
    var episodes: [EpisodeItem] = []
    
    var seasonsDict: [String: [EpisodeItem]] {
        Dictionary(grouping: episodes, by: { $0.season })
    }
    var sortedSeasons: [String] {
        seasonsDict.keys.sorted { s1, s2 in
            let n1 = Int(s1.components(separatedBy: CharacterSet.decimalDigits.inverted).joined()) ?? 0
            let n2 = Int(s2.components(separatedBy: CharacterSet.decimalDigits.inverted).joined()) ?? 0
            return n1 < n2
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Watch Progress & Favorites
// ─────────────────────────────────────────────

struct WatchProgress: Codable, Identifiable {
    var id: String { itemId }
    var itemId: String
    var title: String
    var imageUrl: String
    var episodeId: String
    var episodeTitle: String
    var progressSeconds: Double
    var durationSeconds: Double
    var updatedAt: Date
    
    // Direct playback links
    var videoUrl: String = ""
    var videoUrl1080: String = ""
    var videoUrl360: String = ""
    var subtitleUrl: String = ""
    var subtitleVttUrl: String = ""
}

class WatchProgressStore: ObservableObject {
    static let shared = WatchProgressStore()
    private let key = "UTanWatchProgress_v3"

    @Published var allProgress: [String: WatchProgress] = [:]

    private init() { load() }

    func save(itemId: String, title: String, imageUrl: String,
              episodeId: String, episodeTitle: String,
              progress: Double, duration: Double,
              videoUrl: String, videoUrl1080: String, videoUrl360: String,
              subUrl: String, subVttUrl: String) {
        let record = WatchProgress(
            itemId: itemId, title: title, imageUrl: imageUrl,
            episodeId: episodeId, episodeTitle: episodeTitle,
            progressSeconds: progress, durationSeconds: duration,
            updatedAt: Date(),
            videoUrl: videoUrl, videoUrl1080: videoUrl1080, videoUrl360: videoUrl360,
            subtitleUrl: subUrl, subtitleVttUrl: subVttUrl
        )
        allProgress[itemId] = record
        persist()
    }

    func remove(itemId: String) {
        allProgress.removeValue(forKey: itemId)
        persist()
    }
    
    func clearAll() {
        allProgress.removeAll()
        persist()
    }

    func progress(for itemId: String) -> WatchProgress? { allProgress[itemId] }

    var recent: [WatchProgress] {
        allProgress.values.sorted { $0.updatedAt > $1.updatedAt }
    }

    private func load() {
        guard let data = UserDefaults.standard.data(forKey: key),
              let decoded = try? JSONDecoder().decode([String: WatchProgress].self, from: data)
        else { return }
        allProgress = decoded
    }

    private func persist() {
        if let data = try? JSONEncoder().encode(allProgress) {
            UserDefaults.standard.set(data, forKey: key)
        }
    }
}

class FavoritesStore: ObservableObject {
    static let shared = FavoritesStore()
    private let key = "UTanFavorites_v1"
    
    @Published var items: [VideoItem] = []
    
    private init() { load() }
    
    func toggle(item: VideoItem) {
        if let idx = items.firstIndex(where: { $0.id == item.id }) {
            items.remove(at: idx)
        } else {
            items.insert(item, at: 0)
        }
        persist()
    }
    
    func isFavorite(_ id: String) -> Bool {
        items.contains(where: { $0.id == id })
    }
    
    private func load() {
        if let data = UserDefaults.standard.data(forKey: key),
           let decoded = try? JSONDecoder().decode([VideoItem].self, from: data) {
            items = decoded
        }
    }
    private func persist() {
        if let data = try? JSONEncoder().encode(items) {
            UserDefaults.standard.set(data, forKey: key)
        }
    }
}

// ─────────────────────────────────────────────
// MARK: – Background Downloads Manager
// ─────────────────────────────────────────────

struct DownloadTaskItem: Identifiable, Codable {
    let id: String
    let title: String
    let imageUrl: String
    let isMovie: Bool
    var videoUrl: String
    var subtitleUrl: String
    var progress: Double = 0.0
    var isCompleted: Bool = false
    var localVideoPath: String?
    var localSubPath: String?
}

class DownloadManager: NSObject, ObservableObject, URLSessionDownloadDelegate {
    static let shared = DownloadManager()
    private let key = "UTanDownloads_v1"
    
    @Published var activeDownloads: [DownloadTaskItem] = []
    private var session: URLSession!
    private var taskMap: [Int: String] = [:] // TaskID -> ItemID
    
    private override init() {
        super.init()
        let config = URLSessionConfiguration.background(withIdentifier: "com.mustaqil.utan.background")
        session = URLSession(configuration: config, delegate: self, delegateQueue: nil)
        load()
    }
    
    func startDownload(item: VideoItem, isMovie: Bool, vUrl: String, sUrl: String) {
        guard !activeDownloads.contains(where: { $0.id == item.id }) else { return }
        
        let dl = DownloadTaskItem(id: item.id, title: item.title, imageUrl: item.imageUrl, isMovie: isMovie, videoUrl: vUrl, subtitleUrl: sUrl)
        DispatchQueue.main.async {
            self.activeDownloads.append(dl)
            self.persist()
        }
        
        if let url = URL(string: vUrl) {
            let task = session.downloadTask(with: url)
            taskMap[task.taskIdentifier] = item.id
            task.resume()
        }
    }
    
    func cancel(id: String) {
        DispatchQueue.main.async {
            self.activeDownloads.removeAll(where: { $0.id == id })
            self.persist()
        }
    }
    
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didWriteData bytesWritten: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64) {
        guard let id = taskMap[downloadTask.taskIdentifier], totalBytesExpectedToWrite > 0 else { return }
        let progress = Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
        DispatchQueue.main.async {
            if let idx = self.activeDownloads.firstIndex(where: { $0.id == id }) {
                self.activeDownloads[idx].progress = progress
            }
        }
    }
    
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didFinishDownloadingTo location: URL) {
        guard let id = taskMap[downloadTask.taskIdentifier] else { return }
        
        let dest = FileManager.default.temporaryDirectory.appendingPathComponent(id + ".mp4")
        try? FileManager.default.removeItem(at: dest)
        try? FileManager.default.moveItem(at: location, to: dest)
        
        DispatchQueue.main.async {
            if let idx = self.activeDownloads.firstIndex(where: { $0.id == id }) {
                self.activeDownloads[idx].isCompleted = true
                self.activeDownloads[idx].localVideoPath = dest.path
                self.persist()
                UISaveVideoAtPathToSavedPhotosAlbum(dest.path, nil, nil, nil)
            }
        }
    }
    
    private func load() {
        if let data = UserDefaults.standard.data(forKey: key),
           let d = try? JSONDecoder().decode([DownloadTaskItem].self, from: data) {
            activeDownloads = d
        }
    }
    private func persist() {
        if let data = try? JSONEncoder().encode(activeDownloads) {
            UserDefaults.standard.set(data, forKey: key)
        }
    }
}


// ─────────────────────────────────────────────
// MARK: – Site categories map
// ─────────────────────────────────────────────

struct SiteCategory: Identifiable {
    let id: Int
    let nameAr: String
    let nameEn: String
}

let SITE_CATEGORIES: [SiteCategory] = [
    SiteCategory(id: 0,    nameAr: "أفلام إنجليزية",       nameEn: "English Movies"),
    SiteCategory(id: 1,    nameAr: "مسلسلات أجنبية",       nameEn: "TV Series"),
    SiteCategory(id: 2,    nameAr: "أنمي",                  nameEn: "Anime Series"),
    SiteCategory(id: 3,    nameAr: "بوليوود",               nameEn: "Bollywood Movies"),
    SiteCategory(id: 4,    nameAr: "مسلسلات عربية",        nameEn: "Arabic Series"),
    SiteCategory(id: 5,    nameAr: "مسلسلات آسيوية",       nameEn: "Asian Series"),
    SiteCategory(id: 6,    nameAr: "أفلام آسيوية",         nameEn: "Asian Movies"),
    SiteCategory(id: 7,    nameAr: "أفلام عربية",          nameEn: "Arabic Movies"),
    SiteCategory(id: 8,    nameAr: "مسلسلات بوليوود",      nameEn: "Bollywood Series"),
    SiteCategory(id: 9,    nameAr: "أفلام أنمي",           nameEn: "Anime Movies"),
    SiteCategory(id: 10,   nameAr: "أفلام مكتب الصندوق",   nameEn: "US Box Office"),
    SiteCategory(id: 13,   nameAr: "سينما عربية",          nameEn: "Arabic Cinemas"),
    SiteCategory(id: 14,   nameAr: "أفلام تركية",          nameEn: "Turkish Movies"),
    SiteCategory(id: 15,   nameAr: "مسلسلات تركية",        nameEn: "Turkish Series"),
    SiteCategory(id: 16,   nameAr: "أفلام كرتون",          nameEn: "Cartoon Movies"),
    SiteCategory(id: 17,   nameAr: "مسلسلات كرتون",        nameEn: "Cartoon Series"),
    SiteCategory(id: 18,   nameAr: "أفلام أجنبية",         nameEn: "Foreign Movies"),
    SiteCategory(id: 20,   nameAr: "مسلسلات مدبلجة عربي",  nameEn: "Arabic Dubbed Series"),
    SiteCategory(id: 21,   nameAr: "أفلام مدبلجة عربي",   nameEn: "Arabic Dubbed Movies"),
    SiteCategory(id: 1014, nameAr: "أفلام كردية",          nameEn: "Kurdish Movies"),
    SiteCategory(id: 1015, nameAr: "مسلسلات كردية",        nameEn: "Kurdish Series"),
    SiteCategory(id: 1022, nameAr: "أنمي عربي",            nameEn: "Arabic Anime"),
    SiteCategory(id: 1029, nameAr: "أنمي مدبلج إنجليزي",  nameEn: "English Dubbed Anime"),
]

// ─────────────────────────────────────────────
// MARK: – Main scraper / network layer
// ─────────────────────────────────────────────

class MovieScraper: ObservableObject {
    @Published var heroItems: [VideoItem] = []
    @Published var categories: [(name: String, items: [VideoItem])] = []
    @Published var allItemsPool: [VideoItem] = []
    @Published var isLoading = false

    let baseUrl = "https://movie.vodu.me/"

    func fetchHome() {
        guard let url = URL(string: baseUrl + "index.php") else { return }
        isLoading = true
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { self.isLoading = false }
                return
            }
            let (carouselItems, categoryMap) = Self.parseHome(html: html, base: self.baseUrl)
            DispatchQueue.main.async {
                self.isLoading = false
                self.heroItems = carouselItems
                self.allItemsPool = carouselItems
                self.categories = categoryMap
            }
        }.resume()
    }

    func fetchCategory(typeId: Int, page: Int = 1, completion: @escaping ([VideoItem], Bool) -> Void) {
        let urlStr = "\(baseUrl)index.php?do=list&type=\(typeId)&page=\(page)"
        guard let url = URL(string: urlStr) else { completion([], false); return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([], false) }
                return
            }
            let items = Self.parseListPage(html: html, base: self.baseUrl)
            let hasMore = html.contains("class=\"next\"") || html.contains("»")
            DispatchQueue.main.async { completion(items, hasMore) }
        }.resume()
    }

    func search(query: String, completion: @escaping ([VideoItem]) -> Void) {
        let encoded = query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? query
        let urlStr = "\(baseUrl)index.php?do=list&title=\(encoded)"
        guard let url = URL(string: urlStr) else { completion([]); return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            let items = Self.parseListPage(html: html, base: self.baseUrl)
            DispatchQueue.main.async { completion(items) }
        }.resume()
    }

    func fetchDetails(id: String, completion: @escaping (MediaDetails) -> Void) {
        guard let url = URL(string: "\(baseUrl)index.php?do=view&type=post&id=\(id)") else { return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            var details = MediaDetails()
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { completion(details) }
                return
            }
            details = Self.parseDetails(html: html, base: self.baseUrl)
            DispatchQueue.main.async { completion(details) }
        }.resume()
    }

    // MARK: – HTML parsers (static)

    static func parseHome(html: String, base: String) -> ([VideoItem], [(name: String, items: [VideoItem])]) {
        var carouselItems: [VideoItem] = []
        let carPattern = #"<a href="index\.php\?do=view&type=post&id=(\d+)"><img src="([^"]+)"[^>]*alt="([^"]*)">"#
        if let rx = try? NSRegularExpression(pattern: carPattern, options: []) {
            let ns = html as NSString
            for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if m.numberOfRanges == 4 {
                    let id    = ns.substring(with: m.range(at: 1))
                    var img   = ns.substring(with: m.range(at: 2))
                    let title = ns.substring(with: m.range(at: 3))
                    if !img.hasPrefix("http") { img = base + img }
                    if !carouselItems.contains(where: { $0.id == id }) {
                        carouselItems.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
        }

        var sections: [(name: String, items: [VideoItem])] = []
        let sectionPattern = #"<h3[^>]*>\s*([^<]+)\s*</h3>.*?<div class="homeseries">(.*?)</div>\s*</div>"#
        if let rx = try? NSRegularExpression(pattern: sectionPattern, options: [.dotMatchesLineSeparators]) {
            for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if m.numberOfRanges == 3,
                   let titleR = Range(m.range(at: 1), in: html),
                   let bodyR  = Range(m.range(at: 2), in: html) {
                    let secTitle = html[titleR].trimmingCharacters(in: .whitespacesAndNewlines)
                    let body     = String(html[bodyR])
                    let items    = parseItemXBlock(html: body, base: base)
                    if !items.isEmpty {
                        sections.append((name: secTitle, items: items))
                    }
                }
            }
        }

        if sections.isEmpty && !carouselItems.isEmpty {
            sections = [("الرائج الآن", Array(carouselItems.prefix(10)))]
        }

        return (carouselItems, sections)
    }

    static func parseListPage(html: String, base: String) -> [VideoItem] {
        var items: [VideoItem] = []
        let pattern = #"href="index\.php\?do=view&type=post&id=(\d+)"><img src="([^"]+)"[^>]*>\s*</a>\s*<div class="mytitle">\s*<a[^>]*>([^<]+)</a>"#
        if let rx = try? NSRegularExpression(pattern: pattern, options: [.dotMatchesLineSeparators]) {
            let ns = html as NSString
            for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if m.numberOfRanges == 4 {
                    let id    = ns.substring(with: m.range(at: 1))
                    var img   = ns.substring(with: m.range(at: 2))
                    let title = ns.substring(with: m.range(at: 3)).trimmingCharacters(in: .whitespacesAndNewlines)
                    if !img.hasPrefix("http") { img = base + img }
                    if !items.contains(where: { $0.id == id }) {
                        items.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
        }
        return items
    }

    static func parseItemXBlock(html: String, base: String) -> [VideoItem] {
        var items: [VideoItem] = []
        let itemxPattern = #"<div class="itemx"[^>]*>.*?<img src="([^"]+)".*?<div class="mytitle">([^<]+)</div>"#
        if let rx = try? NSRegularExpression(pattern: itemxPattern, options: [.dotMatchesLineSeparators]) {
            let ns = html as NSString
            var idx = 1
            for m in rx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if m.numberOfRanges == 3 {
                    var img   = ns.substring(with: m.range(at: 1))
                    let title = ns.substring(with: m.range(at: 2)).trimmingCharacters(in: .whitespacesAndNewlines)
                    if !img.hasPrefix("http") { img = base + img }
                    items.append(VideoItem(id: "home_\(idx)_\(title.prefix(10))", title: title, imageUrl: img, type: "post"))
                    idx += 1
                }
            }
        }
        return items
    }

    static func parseDetails(html: String, base: String) -> MediaDetails {
        var d = MediaDetails()

        func first(_ pattern: String, in text: String, opts: NSRegularExpression.Options = []) -> String? {
            guard let rx = try? NSRegularExpression(pattern: pattern, options: opts),
                  let m = rx.firstMatch(in: text, range: NSRange(text.startIndex..., in: text)),
                  m.numberOfRanges >= 2,
                  let r = Range(m.range(at: 1), in: text)
            else { return nil }
            return String(text[r]).trimmingCharacters(in: .whitespacesAndNewlines)
        }

        d.title   = first(#"<h1>(.*?)</h1>"#, in: html) ?? ""
        d.year    = first(#"<span>Year:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.genre   = first(#"<span>Genre:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.rating  = first(#"<span>IMdB Rating:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.runtime = first(#"<span>Runtime:\s*</span>\s*([^<]+)"#, in: html) ?? ""
        d.synopsis = first(#"<h3>Synopsis:</h3>.*?<h4>(.*?)</h4>"#, in: html, opts: [.dotMatchesLineSeparators]) ?? ""

        if let img = first(#"<img src="([^"]+)" class="img-responsive""#, in: html) {
            d.imageUrl = img.hasPrefix("http") ? img : base + img
        }

        var parsedEpisodes: [EpisodeItem] = []
        let episodeBlockPattern = #"<li class="episodeitem">(.*?)</li>"#
        if let blockRx = try? NSRegularExpression(pattern: episodeBlockPattern, options: [.dotMatchesLineSeparators]) {
            for blockMatch in blockRx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if blockMatch.numberOfRanges >= 2,
                   let blockRange = Range(blockMatch.range(at: 1), in: html) {
                    let block = String(html[blockRange])
                    let idPattern = #"data-id="(\d+)"#
                    let titlePattern = #"data-title="([^"]*)"#
                    let urlPattern = #"data-url="([^"]*)"#
                    let url360Pattern = #"data-url360="([^"]*)"#
                    let url1080Pattern = #"data-url1080="([^"]*)"#
                    let srtPattern = #"data-srt="([^"]*)"#
                    let webvttPattern = #"data-webvtt="([^"]*)"#

                    func extract(_ pattern: String, from text: String) -> String {
                        guard let rx = try? NSRegularExpression(pattern: pattern, options: []),
                              let m = rx.firstMatch(in: text, range: NSRange(text.startIndex..., in: text)),
                              m.numberOfRanges >= 2,
                              let r = Range(m.range(at: 1), in: text)
                        else { return "" }
                        return String(text[r]).trimmingCharacters(in: .whitespacesAndNewlines)
                    }

                    let epId = extract(idPattern, from: block)
                    guard !epId.isEmpty else { continue }
                    let epTitle = extract(titlePattern, from: block)
                    let epUrl = extract(urlPattern, from: block)
                    let epUrl360 = extract(url360Pattern, from: block)
                    let epUrl1080 = extract(url1080Pattern, from: block)
                    let epSrt = extract(srtPattern, from: block)
                    let epWebvtt = extract(webvttPattern, from: block)

                    if !epUrl.isEmpty {
                        parsedEpisodes.append(EpisodeItem(
                            id: epId,
                            title: epTitle.isEmpty ? "الحلقة \(parsedEpisodes.count + 1)" : epTitle,
                            url: epUrl,
                            url1080: epUrl1080,
                            url360: epUrl360,
                            subtitleUrl: epSrt,
                            subtitleVttUrl: epWebvtt
                        ))
                    }
                }
            }
        }

        if parsedEpisodes.isEmpty {
            d.isMovie = true
            let moviePattern = #"data-url="([^"]+)"[^>]*data-url360="([^"]*)"[^>]*data-url1080="([^"]*)"[^>]*data-srt="([^"]*)"[^>]*data-webvtt="([^"]*)""#
            if let rx = try? NSRegularExpression(pattern: moviePattern, options: [.dotMatchesLineSeparators]),
               let m = rx.firstMatch(in: html, range: NSRange(html.startIndex..., in: html)),
               m.numberOfRanges >= 6 {
                if let r = Range(m.range(at: 1), in: html) { d.movieUrl = String(html[r]) }
                if let r = Range(m.range(at: 2), in: html) { d.movieUrl360 = String(html[r]) }
                if let r = Range(m.range(at: 3), in: html) { d.movieUrl1080 = String(html[r]) }
                if let r = Range(m.range(at: 4), in: html) { d.movieSubtitleUrl = String(html[r]) }
                if let r = Range(m.range(at: 5), in: html) { d.movieSubtitleVttUrl = String(html[r]) }
            }
        } else {
            d.isMovie = false
            d.episodes = parsedEpisodes
        }

        return d
    }
}

// ─────────────────────────────────────────────
// MARK: – Hex Color Extension
// ─────────────────────────────────────────────
extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 3: (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default: (a, r, g, b) = (1, 1, 1, 0)
        }
        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue:  Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
}
