import Foundation

struct SubtitleCue: Identifiable {
    let id = UUID()
    let startTime: TimeInterval
    let endTime: TimeInterval
    let text: String
}

class SubtitleParser {
    static func parse(url: String, completion: @escaping ([SubtitleCue]) -> Void) {
        guard !url.isEmpty else {
            completion([])
            return
        }
        
        var clean = url
        if !clean.hasPrefix("http") {
            clean = "https://movie.vodu.me/" + clean
        }
        
        guard let urlObj = URL(string: clean) else {
            completion([])
            return
        }
        
        URLSession.shared.dataTask(with: urlObj) { data, _, error in
            guard let data = data, error == nil else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            
            var text: String?
            let encodings: [String.Encoding] = [.utf8, .isoLatin1, .ascii]
            for encoding in encodings {
                if let decoded = String(data: data, encoding: encoding) {
                    text = decoded
                    break
                }
            }
            
            if text == nil {
                let cfEncoding = CFStringEncoding(CFStringEncodings.windowsArabic.rawValue)
                let nsEncoding = CFStringConvertEncodingToNSStringEncoding(cfEncoding)
                let encoding = String.Encoding(rawValue: nsEncoding)
                text = String(data: data, encoding: encoding)
            }
            
            guard let finalText = text else {
                DispatchQueue.main.async { completion([]) }
                return
            }
            
            if finalText.contains("WEBVTT") {
                let cues = parseWebVTT(finalText)
                DispatchQueue.main.async { completion(cues) }
            } else {
                let cues = parseSRT(finalText)
                DispatchQueue.main.async { completion(cues) }
            }
        }.resume()
    }
    
    private static func parseSRT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let blocks = content.components(separatedBy: "\n\n")
        
        for block in blocks {
            let lines = block.components(separatedBy: .newlines)
                .map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }
                .filter { !$0.isEmpty }
            
            guard lines.count >= 3 else { continue }
            
            let timeLine = lines[1]
            let textLines = lines[2...]
            let text = textLines.joined(separator: "\n")
                .replacingOccurrences(of: #"<[^>]+>"#, with: "", options: .regularExpression)
                .trimmingCharacters(in: .whitespacesAndNewlines)
            
            if text.isEmpty { continue }
            
            let times = timeLine.components(separatedBy: " --> ")
            guard times.count == 2,
                  let start = parseSRTTime(times[0]),
                  let end = parseSRTTime(times[1]) else {
                continue
            }
            
            cues.append(SubtitleCue(startTime: start, endTime: end, text: text))
        }
        
        return cues
    }
    
    private static func parseSRTTime(_ timeString: String) -> TimeInterval? {
        let clean = timeString.trimmingCharacters(in: .whitespacesAndNewlines)
        let parts = clean.components(separatedBy: ",")
        guard parts.count == 2,
              let milliseconds = Double(parts[1]) else {
            return nil
        }
        
        let timePart = parts[0]
        let timeComponents = timePart.components(separatedBy: ":")
        guard timeComponents.count == 3,
              let hours = Double(timeComponents[0]),
              let minutes = Double(timeComponents[1]),
              let seconds = Double(timeComponents[2]) else {
            return nil
        }
        
        return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000
    }
    
    private static func parseWebVTT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let lines = content.components(separatedBy: .newlines)
        var i = 0
        
        while i < lines.count {
            let line = lines[i].trimmingCharacters(in: .whitespacesAndNewlines)
            
            if line.contains("-->") {
                let times = line.components(separatedBy: "-->")
                guard times.count == 2,
                      let start = parseVTTTime(times[0]),
                      let end = parseVTTTime(times[1]) else {
                    i += 1
                    continue
                }
                
                var textLines: [String] = []
                i += 1
                while i < lines.count {
                    let nextLine = lines[i].trimmingCharacters(in: .whitespacesAndNewlines)
                    if nextLine.isEmpty { break }
                    textLines.append(nextLine)
                    i += 1
                }
                
                let text = textLines.joined(separator: "\n")
                    .replacingOccurrences(of: #"<[^>]+>"#, with: "", options: .regularExpression)
                    .trimmingCharacters(in: .whitespacesAndNewlines)
                
                if !text.isEmpty {
                    cues.append(SubtitleCue(startTime: start, endTime: end, text: text))
                }
            }
            i += 1
        }
        
        return cues
    }
    
    private static func parseVTTTime(_ timeString: String) -> TimeInterval? {
        let clean = timeString.trimmingCharacters(in: .whitespacesAndNewlines)
        let parts = clean.components(separatedBy: ":")
        
        var hours: Double = 0
        var minutes: Double = 0
        var seconds: Double = 0
        
        if parts.count == 3 {
            hours = Double(parts[0]) ?? 0
            minutes = Double(parts[1]) ?? 0
            let secParts = parts[2].components(separatedBy: ".")
            seconds = Double(secParts[0]) ?? 0
            if secParts.count == 2 {
                seconds += Double(secParts[1])! / 1000
            }
        } else if parts.count == 2 {
            minutes = Double(parts[0]) ?? 0
            let secParts = parts[1].components(separatedBy: ".")
            seconds = Double(secParts[0]) ?? 0
            if secParts.count == 2 {
                seconds += Double(secParts[1])! / 1000
            }
        } else {
            return nil
        }
        
        return hours * 3600 + minutes * 60 + seconds
    }
}
