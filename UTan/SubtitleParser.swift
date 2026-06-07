import Foundation

struct SubtitleItem: Identifiable {
    let id = UUID()
    let start: Double
    let end: Double
    let text: String
}

class SubtitleParser {
    static func parseVTT(_ content: String) -> [SubtitleItem] {
        // Simple VTT parser logic
        return []
    }
}
