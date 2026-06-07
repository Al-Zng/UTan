import Foundation

struct VideoItem: Identifiable, Hashable {
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
    let webvttUrl: String
}

struct MediaDetails {
    var id: String = ""
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
    var movieWebvttUrl: String = ""
    var episodes: [EpisodeItem] = []
}

class MovieScraper: ObservableObject {
    @Published var banners: [VideoItem] = []
    @Published var categories: [String: [VideoItem]] = [:]
    @Published var categoryOrder: [String] = []
    @Published var allItemsPool: [VideoItem] = []
    @Published var isLoading = false
    @Published var searchResults: [VideoItem] = []
    @Published var isSearching = false
    
    let baseUrl = "https://movie.vodu.me/"
    
    func fetchHome() {
        guard let url = URL(string: baseUrl + "index.php") else { return }
        isLoading = true
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { self.isLoading = false }
                return
            }
            
            // 1. Extract Banners
            var extractedBanners: [VideoItem] = []
            let bannerPattern = #"<div class="item[^"]*">.*?<a href="index\.php\?do=view&type=post&id=(\d+)".*?><img src="([^"]+)".*?<div class="mytitle">([^<]+)</div>"#
            if let regex = try? NSRegularExpression(pattern: bannerPattern, options: [.dotMatchesLineSeparators]) {
                let range = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: range)
                for match in matches {
                    if match.numberOfRanges == 4,
                       let idR = Range(match.range(at: 1), in: html),
                       let imgR = Range(match.range(at: 2), in: html),
                       let titleR = Range(match.range(at: 3), in: html) {
                        let id = String(html[idR])
                        var img = String(html[imgR])
                        if !img.hasPrefix("http") { img = self.baseUrl + img }
                        let title = String(html[titleR]).trimmingCharacters(in: .whitespacesAndNewlines)
                        extractedBanners.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
            
            // 2. Extract Categories and Items
            var extractedCategories: [String: [VideoItem]] = [:]
            var order: [String] = []
            let sectionMatches = html.ranges(of: #"<h2><a[^>]*>(.*?)</a></h2>"#, options: .regularExpression)
            
            for i in 0..<sectionMatches.count {
                let matchRange = sectionMatches[i]
                let titleHtml = String(html[matchRange])
                if let titleRegex = try? NSRegularExpression(pattern: #"<h2><a[^>]*>(.*?)</a></h2>"#, options: []),
                   let match = titleRegex.firstMatch(in: titleHtml, options: [], range: NSRange(titleHtml.startIndex..<titleHtml.endIndex, in: titleHtml)),
                   let r = Range(match.range(at: 1), in: titleHtml) {
                    
                    let title = String(titleHtml[r]).trimmingCharacters(in: .whitespacesAndNewlines)
                    let startPos = matchRange.upperBound
                    let endPos = (i + 1 < sectionMatches.count) ? sectionMatches[i+1].lowerBound : html.endIndex
                    let sectionContent = String(html[startPos..<endPos])
                    
                    if let contentMatch = sectionContent.range(of: #"<div class="homeseries">(.*?)</div>\s*</div>\s*</div>"#, options: .regularExpression) {
                        let innerContent = String(sectionContent[contentMatch])
                        var items: [VideoItem] = []
                        let itemPattern = #"<a href="index\.php\?do=view&type=post&id=(\d+)".*?<img src="([^"]+)".*?<div class="mytitle">([^<]+)</div>"#
                        if let itemRegex = try? NSRegularExpression(pattern: itemPattern, options: [.dotMatchesLineSeparators]) {
                            let matches = itemRegex.matches(in: innerContent, options: [], range: NSRange(innerContent.startIndex..<innerContent.endIndex, in: innerContent))
                            for m in matches {
                                if m.numberOfRanges == 4,
                                   let idR = Range(m.range(at: 1), in: innerContent),
                                   let imgR = Range(m.range(at: 2), in: innerContent),
                                   let titleR = Range(m.range(at: 3), in: innerContent) {
                                    let id = String(innerContent[idR])
                                    var img = String(innerContent[imgR])
                                    if !img.hasPrefix("http") { img = self.baseUrl + img }
                                    let itemTitle = String(innerContent[titleR]).trimmingCharacters(in: .whitespacesAndNewlines)
                                    items.append(VideoItem(id: id, title: itemTitle, imageUrl: img, type: "post"))
                                }
                            }
                        }
                        if !items.isEmpty {
                            extractedCategories[title] = items
                            order.append(title)
                        }
                    }
                }
            }
            
            DispatchQueue.main.async {
                self.isLoading = false
                self.banners = extractedBanners
                self.categories = extractedCategories
                self.categoryOrder = order
                self.allItemsPool = Array(Set(extractedBanners + extractedCategories.values.flatMap { $0 }))
            }
        }.resume()
    }
    
    func search(query: String) {
        guard !query.isEmpty else {
            DispatchQueue.main.async { self.searchResults = [] }
            return
        }
        
        let encodedQuery = query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? ""
        guard let url = URL(string: baseUrl + "index.php?do=list&title=" + encodedQuery) else { return }
        
        isSearching = true
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { self.isSearching = false }
                return
            }
            
            var items: [VideoItem] = []
            let pattern = #"<div class="itemx"[^>]*>.*?<a href="index\.php\?do=view&type=post&id=(\d+)".*?<img src="([^"]+)".*?<div class="mytitle">([^<]+)</div>"#
            if let regex = try? NSRegularExpression(pattern: pattern, options: [.dotMatchesLineSeparators]) {
                let range = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: range)
                for match in matches {
                    if match.numberOfRanges == 4,
                       let idR = Range(match.range(at: 1), in: html),
                       let imgR = Range(match.range(at: 2), in: html),
                       let titleR = Range(match.range(at: 3), in: html) {
                        let id = String(html[idR])
                        var img = String(html[imgR])
                        if !img.hasPrefix("http") { img = self.baseUrl + img }
                        let title = String(html[titleR]).trimmingCharacters(in: .whitespacesAndNewlines)
                        items.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
            
            DispatchQueue.main.async {
                self.isSearching = false
                self.searchResults = items
            }
        }.resume()
    }
    
    func fetchDetails(id: String, completion: @escaping (MediaDetails) -> Void) {
        guard let url = URL(string: baseUrl + "index.php?do=view&type=post&id=\(id)") else { return }
        
        URLSession.shared.dataTask(with: url) { data, _, _ in
            var details = MediaDetails()
            details.id = id
            
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                completion(details)
                return
            }
            
            // Basic Details
            if let titleRegex = try? NSRegularExpression(pattern: #"<h1>(.*?)</h1>"#, options: []),
               let match = titleRegex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)),
               let range = Range(match.range(at: 1), in: html) {
                details.title = String(html[range]).trimmingCharacters(in: .whitespacesAndNewlines)
            }
            
            let synPattern = #"<h3>Synopsis:</h3>.*?<h4>(.*?)</h4>"#
            if let regex = try? NSRegularExpression(pattern: synPattern, options: [.dotMatchesLineSeparators]),
               let match = regex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)),
               let range = Range(match.range(at: 1), in: html) {
                details.synopsis = String(html[range]).trimmingCharacters(in: .whitespacesAndNewlines)
            }
            
            let metadataKeys = ["Year": #"<span>Year: </span>\s*([^<]+)"#,
                                "Genre": #"<span>Genre: </span>\s*([^<]+)"#,
                                "Rating": #"<span>IMdB Rating: </span>\s*([^<]+)"#,
                                "Runtime": #"<span>Runtime:\s*</span>\s*([^<]+)"#]
            
            for (key, pat) in metadataKeys {
                if let regex = try? NSRegularExpression(pattern: pat, options: []),
                   let match = regex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)),
                   let range = Range(match.range(at: 1), in: html) {
                    let val = String(html[range]).trimmingCharacters(in: .whitespacesAndNewlines)
                    if key == "Year" { details.year = val }
                    if key == "Genre" { details.genre = val }
                    if key == "Rating" { details.rating = val }
                    if key == "Runtime" { details.runtime = val }
                }
            }
            
            if let imgRegex = try? NSRegularExpression(pattern: #"<img src="([^"]+)" class="img-responsive""#, options: []),
               let match = imgRegex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)),
               let range = Range(match.range(at: 1), in: html) {
                var img = String(html[range])
                if !img.hasPrefix("http") { img = self.baseUrl + img }
                details.imageUrl = img
            }
            
            // Episodes/Movie Data
            var parsedEpisodes: [EpisodeItem] = []
            let epPattern = #"data-webvtt="([^"]*)"\s*data-srt="([^"]*)"\s*data-token="[^"]*"\s*data-id="(\d+)"\s*data-cookie="[^"]*"\s*data-title="([^"]*)"\s*data-url="([^"]*)"\s*data-url360="([^"]*)"\s*data-url1080="([^"]*)""#
            
            if let regex = try? NSRegularExpression(pattern: epPattern, options: [.dotMatchesLineSeparators]) {
                let range = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: range)
                for match in matches {
                    if match.numberOfRanges >= 8,
                       let vttR = Range(match.range(at: 1), in: html),
                       let srtR = Range(match.range(at: 2), in: html),
                       let idR = Range(match.range(at: 3), in: html),
                       let titleR = Range(match.range(at: 4), in: html),
                       let urlR = Range(match.range(at: 5), in: html),
                       let url360R = Range(match.range(at: 6), in: html),
                       let url1080R = Range(match.range(at: 7), in: html) {
                        
                        let epItem = EpisodeItem(
                            id: String(html[idR]),
                            title: String(html[titleR]).isEmpty ? "Episode \(parsedEpisodes.count + 1)" : String(html[titleR]),
                            url: String(html[urlR]),
                            url1080: String(html[url1080R]),
                            url360: String(html[url360R]),
                            subtitleUrl: String(html[srtR]),
                            webvttUrl: String(html[vttR])
                        )
                        parsedEpisodes.append(epItem)
                    }
                }
            }
            
            if parsedEpisodes.isEmpty {
                details.isMovie = true
                let moviePattern = #"data-webvtt="([^"]*)"\s*data-srt="([^"]*)"\s*data-token="[^"]*"\s*data-id="(\d+)"\s*data-cookie="[^"]*"\s*data-title="([^"]*)"\s*data-url="([^"]*)"\s*data-url360="([^"]*)"\s*data-url1080="([^"]*)""#
                if let regex = try? NSRegularExpression(pattern: moviePattern, options: [.dotMatchesLineSeparators]),
                   let match = regex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)) {
                    if let vttR = Range(match.range(at: 1), in: html) { details.movieWebvttUrl = String(html[vttR]) }
                    if let srtR = Range(match.range(at: 2), in: html) { details.movieSubtitleUrl = String(html[srtR]) }
                    if let urlR = Range(match.range(at: 5), in: html) { details.movieUrl = String(html[urlR]) }
                    if let url360R = Range(match.range(at: 6), in: html) { details.movieUrl360 = String(html[url360R]) }
                    if let url1080R = Range(match.range(at: 7), in: html) { details.movieUrl1080 = String(html[url1080R]) }
                }
            } else {
                details.isMovie = false
                details.episodes = parsedEpisodes
            }
            
            DispatchQueue.main.async {
                completion(details)
            }
        }.resume()
    }
}

extension String {
    func ranges(of substring: String, options: CompareOptions = [], locale: Locale? = nil) -> [Range<Index>] {
        var ranges: [Range<Index>] = []
        while let range = self.range(of: substring, options: options, range: (ranges.last?.upperBound ?? self.startIndex)..<self.endIndex, locale: locale) {
            ranges.append(range)
        }
        return ranges
    }
}
