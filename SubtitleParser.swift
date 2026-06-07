import Foundation

struct SubtitleCue: Identifiable {
    let id = UUID()
    let startTime: TimeInterval
    let endTime: TimeInterval
    let text: String
}

class SubtitleParser {
    static func parse(url: String, completion: @escaping ([SubtitleCue]) -> Void) {
        if url.isEmpty {
            completion([])
            return
        }
        var cleanUrl = url
        if !cleanUrl.hasPrefix("http") {
            cleanUrl = "https://movie.vodu.me/" + cleanUrl
        }
        guard let urlObj = URL(string: cleanUrl) else {
            completion([])
            return
        }
        URLSession.shared.dataTask(with: urlObj) { data, _, _ in
            guard let data = data, let text = String(data: data, encoding: .utf8) else {
                completion([])
                return
            }
            let cues = parseContent(text)
            DispatchQueue.main.async {
                completion(cues)
            }
        }.resume()
    }
    
    private static func parseContent(_ text: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let lines = text.components(separatedBy: .newlines).map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
        
        var currentStart: TimeInterval?
        var currentEnd: TimeInterval?
        var currentText = ""
        
        for line in lines {
            if line.isEmpty {
                if let start = currentStart, let end = currentEnd, !currentText.isEmpty {
                    cues.append(SubtitleCue(startTime: start, endTime: end, text: currentText.trimmingCharacters(in: .whitespacesAndNewlines)))
                }
                currentStart = nil
                currentEnd = nil
                currentText = ""
                continue
            }
            
            if line.contains("-->") {
                let parts = line.components(separatedBy: "-->")
                if parts.count == 2 {
                    currentStart = parseTime(parts[0])
                    currentEnd = parseTime(parts[1])
                }
            } else if Int(line) != nil {
                continue
            } else if line != "WEBVTT" {
                if currentText.isEmpty {
                    currentText = line
                } else {
                    currentText += "\n" + line
                }
            }
        }
        
        if let start = currentStart, let end = currentEnd, !currentText.isEmpty {
            cues.append(SubtitleCue(startTime: start, endTime: end, text: currentText))
        }
        
        return cues
    }
    
    private static func parseTime(_ timeStr: String) -> TimeInterval? {
        let cleanStr = timeStr.trimmingCharacters(in: .whitespacesAndNewlines).replacingOccurrences(of: ",", with: ".")
        let parts = cleanStr.components(separatedBy: ":")
        guard parts.count >= 2 else { return nil }
        
        var hours: Double = 0.0
        var minutes: Double = 0.0
        var seconds: Double = 0.0
        
        if parts.count == 3 {
            hours = Double(parts[0]) ?? 0.0
            minutes = Double(parts[1]) ?? 0.0
            seconds = Double(parts[2]) ?? 0.0
        } else if parts.count == 2 {
            minutes = Double(parts[0]) ?? 0.0
            seconds = Double(parts[1]) ?? 0.0
        }
        
        return (hours * 3600.0) + (minutes * 60.0) + seconds
    }
}
