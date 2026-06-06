import os

# Create directory structure
os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# 1. Write project.pbxproj
pbxproj_content = """// !$*UTF8*$!
{
	archiveVersion = 1;
	classes = {
	};
	objectVersion = 56;
	objects = {

/* Begin PBXBuildFile section */
		010101012C12345600000001 /* UTanApp.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000002 /* UTanApp.swift */; };
		010101012C12345600000003 /* Scraper.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000004 /* Scraper.swift */; };
		010101012C12345600000005 /* CustomPlayer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000006 /* CustomPlayer.swift */; };
		010101012C12345600000007 /* SubtitleParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000008 /* SubtitleParser.swift */; };
		010101012C12345600000009 /* Views.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000000A /* Views.swift */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		010101012C12345600000002 /* UTanApp.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = UTanApp.swift; sourceTree = "<group>"; };
		010101012C12345600000004 /* Scraper.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Scraper.swift; sourceTree = "<group>"; };
		010101012C12345600000006 /* CustomPlayer.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = CustomPlayer.swift; sourceTree = "<group>"; };
		010101012C12345600000008 /* SubtitleParser.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = SubtitleParser.swift; sourceTree = "<group>"; };
		010101012C1234560000000A /* Views.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Views.swift; sourceTree = "<group>"; };
		010101012C1234560000000B /* Info.plist */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
		010101012C1234560000000C /* UTan.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = UTan.app; sourceTree = BUILT_PRODUCTS_DIR; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		010101012C1234560000000D /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		010101012C1234560000000E /* MainGroup */ = {
			isa = PBXGroup;
			children = (
				010101012C1234560000000F /* UTan */,
				010101012C1234560000000C /* UTan.app */,
			);
			sourceTree = "<group>";
		};
		010101012C1234560000000F /* UTan */ = {
			isa = PBXGroup;
			children = (
				010101012C12345600000002 /* UTanApp.swift */,
				010101012C12345600000004 /* Scraper.swift */,
				010101012C12345600000006 /* CustomPlayer.swift */,
				010101012C12345600000008 /* SubtitleParser.swift */,
				010101012C1234560000000A /* Views.swift */,
				010101012C1234560000000B /* Info.plist */,
			);
			path = UTan;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		010101012C12345600000010 /* UTan */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 010101012C12345600000011 /* Build configuration list for PBXNativeTarget "UTan" */;
			buildPhases = (
				010101012C12345600000012 /* Sources */,
				010101012C1234560000000D /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = UTan;
			productName = UTan;
			productReference = 010101012C1234560000000C /* UTan.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		010101012C12345600000013 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				LastSwiftUpdateCheck = 1500;
				LastUpgradeCheck = 1500;
				TargetAttributes = {
					010101012C12345600000010 = {
						CreatedOnToolsVersion = 15.0;
						DevelopmentTeam = "";
					};
				};
			};
			buildConfigurationList = 010101012C12345600000014 /* Build configuration list for PBXProject "UTan" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = 010101012C1234560000000E /* MainGroup */;
			productRefGroup = 010101012C1234560000000E /* MainGroup */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				010101012C12345600000010 /* UTan */,
			);
		};
/* End PBXProject section */

/* Begin PBXSourcesBuildPhase section */
		010101012C12345600000012 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				010101012C12345600000001 /* UTanApp.swift in Sources */,
				010101012C12345600000003 /* Scraper.swift in Sources */,
				010101012C12345600000005 /* CustomPlayer.swift in Sources */,
				010101012C12345600000007 /* SubtitleParser.swift in Sources */,
				010101012C12345600000009 /* Views.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		010101012C12345600000015 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_AUDIT_TEXT_INCLUSION_IN_SHMEM_DISABLE = YES;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = dwarf;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				ENABLE_TESTABILITY = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_DYNAMIC_NO_PIC = NO;
				GCC_NO_COMMON_BLOCKS = YES;
				GCC_OPTIMIZATION_LEVEL = 0;
				GCC_PREPROCESSOR_DEFINITIONS = (
					"DEBUG=1",
					"$(inherited)",
				);
				MTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
				MTL_FAST_MATH = YES;
				ONLY_ACTIVE_ARCH = YES;
				SDKROOT = iphoneos;
				SWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
				SWIFT_OPTIMIZATION_LEVEL = "-Onone";
			};
			name = Debug;
		};
		010101012C12345600000016 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ALWAYS_SEARCH_USER_PATHS = NO;
				CLANG_ANALYZER_NONNULL = YES;
				CLANG_AUDIT_TEXT_INCLUSION_IN_SHMEM_DISABLE = YES;
				CLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
				CLANG_ENABLE_MODULES = YES;
				CLANG_ENABLE_OBJC_ARC = YES;
				CLANG_ENABLE_OBJC_WEAK = YES;
				COPY_PHASE_STRIP = NO;
				DEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
				ENABLE_NS_ASSERTIONS = NO;
				ENABLE_STRICT_OBJC_MSGSEND = YES;
				GCC_C_LANGUAGE_STANDARD = gnu11;
				GCC_NO_COMMON_BLOCKS = YES;
				MTL_FAST_MATH = YES;
				SDKROOT = iphoneos;
				SWIFT_COMPILATION_MODE = wholemodule;
				SWIFT_OPTIMIZATION_LEVEL = "-O";
				VALIDATE_PRODUCT = YES;
			};
			name = Release;
		};
		010101012C12345600000017 /* Debug */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Manual;
				CODE_SIGNING_ALLOWED = NO;
				CODE_SIGNING_REQUIRED = NO;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "";
				ENABLE_PREVIEWS = YES;
				INFOPLIST_FILE = UTan/Info.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 15.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Debug;
		};
		010101012C12345600000018 /* Release */ = {
			isa = XCBuildConfiguration;
			buildSettings = {
				ASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
				ASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
				CODE_SIGN_STYLE = Manual;
				CODE_SIGNING_ALLOWED = NO;
				CODE_SIGNING_REQUIRED = NO;
				CURRENT_PROJECT_VERSION = 1;
				DEVELOPMENT_ASSET_PATHS = "";
				ENABLE_PREVIEWS = YES;
				INFOPLIST_FILE = UTan/Info.plist;
				IPHONEOS_DEPLOYMENT_TARGET = 15.0;
				LD_RUNPATH_SEARCH_PATHS = (
					"$(inherited)",
					"@executable_path/Frameworks",
				);
				MARKETING_VERSION = 1.0;
				PRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
				PRODUCT_NAME = "$(TARGET_NAME)";
				SWIFT_EMIT_LOC_STRINGS = YES;
				SWIFT_VERSION = 5.0;
				TARGETED_DEVICE_FAMILY = "1,2";
			};
			name = Release;
		};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
		010101012C12345600000011 /* Build configuration list for PBXNativeTarget "UTan" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				010101012C12345600000017 /* Debug */,
				010101012C12345600000018 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		010101012C12345600000014 /* Build configuration list for PBXProject "UTan" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				010101012C12345600000015 /* Debug */,
				010101012C12345600000016 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 010101012C12345600000013 /* Project object */;
}
"""

with open("UTan/UTan.xcodeproj/project.pbxproj", "w", encoding="utf-8") as f:
    f.write(pbxproj_content)

# 2. Write Info.plist
info_plist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
	<key>CFBundleDevelopmentRegion</key>
	<string>en</string>
	<key>CFBundleExecutable</key>
	<string>$(EXECUTABLE_NAME)</string>
	<key>CFBundleIdentifier</key>
	<string>com.mustaqil.utan</string>
	<key>CFBundleInfoDictionaryVersion</key>
	<string>6.0</string>
	<key>CFBundleName</key>
	<string>UTan</string>
	<key>CFBundlePackageType</key>
	<string>APPL</string>
	<key>CFBundleShortVersionString</key>
	<string>1.0</string>
	<key>CFBundleVersion</key>
	<string>1</string>
	<key>LSRequiresIPhoneOS</key>
	<true/>
	<key>NSAppTransportSecurity</key>
	<dict>
		<key>NSAllowsArbitraryLoads</key>
		<true/>
	</dict>
	<key>UILaunchScreen</key>
	<dict/>
	<key>UISupportedInterfaceOrientations</key>
	<array>
		<string>UIInterfaceOrientationPortrait</string>
		<string>UIInterfaceOrientationLandscapeLeft</string>
		<string>UIInterfaceOrientationLandscapeRight</string>
	</array>
</dict>
</plist>
"""

with open("UTan/UTan/Info.plist", "w", encoding="utf-8") as f:
    f.write(info_plist)

# 3. Write UTanApp.swift
app_swift = """import SwiftUI

@main
struct UTanApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}
"""

with open("UTan/UTan/UTanApp.swift", "w", encoding="utf-8") as f:
    f.write(app_swift)

# 4. Write Scraper.swift
scraper_swift = r"""import Foundation

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
    var movieSubtitleUrl: String = ""
    var episodes: [EpisodeItem] = []
}

class MovieScraper: ObservableObject {
    @Published var heroItem: VideoItem?
    @Published var categories: [String: [VideoItem]] = [:]
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
            
            var items: [VideoItem] = []
            let pattern = #"<div class="itemx"[^>]*>.*?<a href="index\.php\?do=view&type=post&id=(\d+)".*?<img src="([^"]+)".*?<div class="mytitle">([^<]+)</div>"#
            if let regex = try? NSRegularExpression(pattern: pattern, options: [.dotMatchesLineSeparators]) {
                let range = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: range)
                
                for match in matches {
                    if match.numberOfRanges == 4,
                       let idRange = Range(match.range(at: 1), in: html),
                       let imgRange = Range(match.range(at: 2), in: html),
                       let titleRange = Range(match.range(at: 3), in: html) {
                        
                        let id = String(html[idRange])
                        var img = String(html[imgRange])
                        if !img.hasPrefix("http") { img = self.baseUrl + img }
                        let title = String(html[titleRange]).trimmingCharacters(in: .whitespacesAndNewlines)
                        
                        items.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
            
            DispatchQueue.main.async {
                self.isLoading = false
                if !items.isEmpty {
                    self.heroItem = items.first
                    self.categories["Anime Series"] = Array(items.prefix(min(items.count, 6)))
                    if items.count > 6 {
                        self.categories["Latest Additions"] = Array(items.suffix(items.count - 6))
                    } else {
                        self.categories["Trending Content"] = items
                    }
                }
            }
        }.resume()
    }
    
    func fetchDetails(id: String, completion: @escaping (MediaDetails) -> Void) {
        guard let url = URL(string: baseUrl + "index.php?do=view&type=post&id=\(id)") else { return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            var details = MediaDetails()
            details.title = "UTan Video Media"
            
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                completion(details)
                return
            }
            
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
            
            var parsedEpisodes: [EpisodeItem] = []
            let epPattern = #"data-srt="([^"]*)"[^>]*data-id="(\d+)"[^>]*data-title="([^"]*)"\s*data-url="([^"]*)"[^>]*data-url360="([^"]*)"\s*data-url1080="([^"]*)""#
            
            if let regex = try? NSRegularExpression(pattern: epPattern, options: [.dotMatchesLineSeparators]) {
                let range = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: range)
                
                for match in matches {
                    if match.numberOfRanges >= 7,
                       let srtR = Range(match.range(at: 1), in: html),
                       let idR = Range(match.range(at: 2), in: html),
                       let titleR = Range(match.range(at: 3), in: html),
                       let urlR = Range(match.range(at: 4), in: html),
                       let url360R = Range(match.range(at: 5), in: html),
                       let url1080R = Range(match.range(at: 6), in: html) {
                        
                        let epItem = EpisodeItem(
                            id: String(html[idR]),
                            title: String(html[titleR]).isEmpty ? "Episode \(parsedEpisodes.count + 1)" : String(html[titleR]),
                            url: String(html[urlR]),
                            url1080: String(html[url1080R]),
                            url360: String(html[url360R]),
                            subtitleUrl: String(html[srtR])
                        )
                        parsedEpisodes.append(epItem)
                    }
                }
            }
            
            if parsedEpisodes.isEmpty {
                details.isMovie = true
                let singleUrlPattern = #"data-url="([^"]+)".*?data-srt="([^"]*)""#
                if let regex = try? NSRegularExpression(pattern: singleUrlPattern, options: [.dotMatchesLineSeparators]),
                   let match = regex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)) {
                    if let urlR = Range(match.range(at: 1), in: html) {
                        details.movieUrl = String(html[urlR])
                    }
                    if match.numberOfRanges >= 3, let srtR = Range(match.range(at: 2), in: html) {
                        details.movieSubtitleUrl = String(html[srtR])
                    }
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
"""

with open("UTan/UTan/Scraper.swift", "w", encoding="utf-8") as f:
    f.write(scraper_swift)

# 5. Write SubtitleParser.swift
sub_parser_swift = """import Foundation

struct SubtitleCue: Identifiable {
    let id = UUID()
    let startTime: TimeInterval
    let endTime: TimeInterval
    let text: String
}

class SubtitleParser {
    static func parse(url: String, completion: @escaping ([SubtitleCue]) -> Void) {
        guard let urlObj = URL(string: url) else {
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
                    currentText += "\\n" + line
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
"""

with open("UTan/UTan/SubtitleParser.swift", "w", encoding="utf-8") as f:
    f.write(sub_parser_swift)

# 6. Write CustomPlayer.swift
player_swift = """import SwiftUI
import AVKit

enum SubtitleFontFamily: String, CaseIterable, Identifiable {
    case system = "System Default"
    case monospaced = "Monospaced Pro"
    case serif = "Serif Elegant"
    case rounded = "Rounded Modern"
    
    var id: String { self.rawValue }
}

enum SubtitleColor: String, CaseIterable, Identifiable {
    case white = "White"
    case yellow = "Gold Yellow"
    case cyan = "Cyan Blue"
    case green = "Neon Green"
    
    var id: String { self.rawValue }
    
    var color: Color {
        switch self {
        case .white: return .white
        case .yellow: return .yellow
        case .cyan: return .cyan
        case .green: return .green
        }
    }
}

struct VideoPlayerRepresentable: UIViewControllerRepresentable {
    let player: AVPlayer
    
    func makeUIViewController(context: Context) -> AVPlayerViewController {
        let controller = AVPlayerViewController()
        controller.player = player
        controller.showsPlaybackControls = false
        controller.videoGravity = .resizeAspect
        return controller
    }
    
    func updateUIViewController(_ uiViewController: AVPlayerViewController, context: Context) {}
}

struct CustomPlayerView: View {
    let videoUrl: String
    let subtitleUrl: String
    
    @Environment(\\.presentationMode) var presentationMode
    @State private var player: AVPlayer?
    @State private var isPlaying = true
    @State private var currentTime: TimeInterval = 0
    @State private var duration: TimeInterval = 0
    @State private var cues: [SubtitleCue] = []
    @State private var activeSubtitleText = ""
    @State private var isSpeedUpActive = false
    @State private var showSettings = false
    
    // Subtitle Customizations
    @State private var fontSize: CGFloat = 20
    @State private var fontColor: SubtitleColor = .white
    @State private var fontFamily: SubtitleFontFamily = .system
    @State private var verticalOffset: CGFloat = 40
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            if let player = player {
                VideoPlayerRepresentable(player: player)
                    .ignoresSafeArea()
                    .onLongPressGesture(minimumDuration: 0.3, pressing: { isPressing in
                        if isPressing {
                            self.isSpeedUpActive = true
                            player.rate = 2.0
                        } else {
                            self.isSpeedUpActive = false
                            player.rate = self.isPlaying ? 1.0 : 0.0
                        }
                    }, perform: {})
                
                VStack {
                    Spacer()
                    if !activeSubtitleText.isEmpty {
                        Text(activeSubtitleText)
                            .font(getCustomFont())
                            .foregroundColor(fontColor.color)
                            .shadow(color: .black, radius: 4, x: 2, y: 2)
                            .padding(.horizontal, 14)
                            .padding(.vertical, 6)
                            .background(Color.black.opacity(0.5))
                            .cornerRadius(8)
                            .multilineTextAlignment(.center)
                            .padding(.bottom, verticalOffset)
                    }
                }
                .padding(.horizontal, 20)
                .ignoresSafeArea()
                
                if isSpeedUpActive {
                    VStack {
                        HStack {
                            Image(systemName: "forward.fill")
                            Text("2.0X Speed")
                                .bold()
                        }
                        .foregroundColor(.white)
                        .padding(10)
                        .background(Color.black.opacity(0.6))
                        .cornerRadius(20)
                        .padding(.top, 40)
                        Spacer()
                    }
                }
                
                VStack {
                    HStack {
                        Button(action: {
                            player.pause()
                            presentationMode.wrappedValue.dismiss()
                        }) {
                            Image(systemName: "chevron.left")
                                .font(.title2)
                                .foregroundColor(.white)
                                .padding(12)
                                .background(Color.black.opacity(0.4))
                                .clipShape(Circle())
                        }
                        Spacer()
                        
                        Button(action: { showSettings.toggle() }) {
                            Image(systemName: "captions.bubble.fill")
                                .font(.title2)
                                .foregroundColor(.white)
                                .padding(12)
                                .background(Color.black.opacity(0.4))
                                .clipShape(Circle())
                        }
                    }
                    .padding(.horizontal)
                    .padding(.top, 20)
                    
                    Spacer()
                    
                    VStack(spacing: 12) {
                        HStack {
                            Text(formatTime(currentTime))
                                .font(.caption)
                                .foregroundColor(.white)
                            
                            Slider(value: $currentTime, in: 0...max(duration, 1), onEditingChanged: { editing in
                                if !editing {
                                    player.seek(to: CMTime(seconds: currentTime, preferredTimescale: 600))
                                }
                            })
                            .accentColor(.red)
                            
                            Text(formatTime(duration))
                                .font(.caption)
                                .foregroundColor(.white)
                        }
                        .padding(.horizontal)
                        
                        HStack(spacing: 40) {
                            Button(action: {
                                let targetTime = max(0, currentTime - 10)
                                player.seek(to: CMTime(seconds: targetTime, preferredTimescale: 600))
                            }) {
                                Image(systemName: "backward.10")
                                    .font(.title)
                                    .foregroundColor(.white)
                            }
                            
                            Button(action: {
                                if isPlaying {
                                    player.pause()
                                } else {
                                    player.play()
                                }
                                isPlaying.toggle()
                            }) {
                                Image(systemName: isPlaying ? "pause.fill" : "play.fill")
                                    .font(.system(size: 44))
                                    .foregroundColor(.white)
                            }
                            
                            Button(action: {
                                let targetTime = min(duration, currentTime + 10)
                                player.seek(to: CMTime(seconds: targetTime, preferredTimescale: 600))
                            }) {
                                Image(systemName: "forward.10")
                                    .font(.title)
                                    .foregroundColor(.white)
                            }
                        }
                        .padding(.bottom, 20)
                    }
                    .background(
                        LinearGradient(colors: [.clear, .black.opacity(0.7)], startPoint: .top, endPoint: .bottom)
                    )
                }
            }
        }
        .onAppear {
            setupPlayer()
        }
        .sheet(isPresented: $showSettings) {
            SubtitleSettingsView(fontSize: $fontSize, fontColor: $fontColor, fontFamily: $fontFamily, verticalOffset: $verticalOffset)
        }
    }
    
    private func setupPlayer() {
        guard let url = URL(string: videoUrl) else { return }
        let playerItem = AVPlayerItem(url: url)
        let newPlayer = AVPlayer(playerItem: playerItem)
        self.player = newPlayer
        newPlayer.play()
        
        NotificationCenter.default.addObserver(forName: .AVPlayerItemDidPlayToEndTime, object: playerItem, queue: .main) { _ in
            self.isPlaying = false
        }
        
        let asset = playerItem.asset
        Task {
            if let dur = try? await asset.load(.duration) {
                DispatchQueue.main.async {
                    self.duration = dur.seconds
                }
            }
        }
        
        newPlayer.addPeriodicTimeObserver(forInterval: CMTime(seconds: 0.2, preferredTimescale: 600), queue: .main) { time in
            self.currentTime = time.seconds
            if let activeCue = cues.first(where: { time.seconds >= $0.startTime && time.seconds <= $0.endTime }) {
                self.activeSubtitleText = activeCue.text
            } else {
                self.activeSubtitleText = ""
            }
        }
        
        if !subtitleUrl.isEmpty {
            SubtitleParser.parse(url: subtitleUrl) { parsedCues in
                self.cues = parsedCues
            }
        }
    }
    
    private func getCustomFont() -> Font {
        switch fontFamily {
        case .system: return .system(size: fontSize, weight: .semibold, design: .default)
        case .monospaced: return .system(size: fontSize, weight: .semibold, design: .monospaced)
        case .serif: return .system(size: fontSize, weight: .semibold, design: .serif)
        case .rounded: return .system(size: fontSize, weight: .semibold, design: .rounded)
        }
    }
    
    private func formatTime(_ seconds: TimeInterval) -> String {
        let mins = Int(seconds) / 60
        let secs = Int(seconds) % 60
        return String(format: "%02d:%02d", mins, secs)
    }
}

struct SubtitleSettingsView: View {
    @Binding var fontSize: CGFloat
    @Binding var fontColor: SubtitleColor
    @Binding var fontFamily: SubtitleFontFamily
    @Binding var verticalOffset: CGFloat
    
    @Environment(\\.presentationMode) var presentationMode
    
    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Font Size / حجم الخط")) {
                    Slider(value: $fontSize, in: 14...34, step: 1)
                    Text("Current Size: \\(Int(fontSize)) px")
                }
                
                Section(header: Text("Font Color / لون الخط")) {
                    Picker("Select Color", selection: $fontColor) {
                        ForEach(SubtitleColor.allCases) { color in
                            Text(color.rawValue).tag(color)
                        }
                    }
                    .pickerStyle(SegmentedPickerStyle())
                }
                
                Section(header: Text("Font Family / نوع الخط")) {
                    Picker("Select Family", selection: $fontFamily) {
                        ForEach(SubtitleFontFamily.allCases) { family in
                            Text(family.rawValue).tag(family)
                        }
                    }
                }
                
                Section(header: Text("Vertical Position / مكان الترجمة")) {
                    Slider(value: $verticalOffset, in: 10...150, step: 5)
                    Text("Bottom Safe Offset: \\(Int(verticalOffset)) pt")
                }
            }
            .navigationTitle("Subtitle Panel")
            .navigationBarItems(trailing: Button("Done") {
                presentationMode.wrappedValue.dismiss()
            })
        }
    }
}
"""

with open("UTan/UTan/CustomPlayer.swift", "w", encoding="utf-8") as f:
    f.write(player_swift)

# 7. Write Views.swift
views_swift = """import SwiftUI

struct ContentView: View {
    @StateObject private var scraper = MovieScraper()
    @State private var searchText = ""
    
    var body: some View {
        NavigationView {
            ZStack {
                Color(red: 0.08, green: 0.09, blue: 0.12).ignoresSafeArea()
                
                if scraper.isLoading {
                    ProgressView("Loading UTan Media Content...")
                        .progressViewStyle(CircularProgressViewStyle(tint: .red))
                        .foregroundColor(.white)
                } else {
                    ScrollView {
                        VStack(alignment: .leading, spacing: 20) {
                            HStack {
                                Image(systemName: "magnifyingglass")
                                    .foregroundColor(.gray)
                                TextField("Search Movies & Anime...", text: $searchText)
                                    .foregroundColor(.white)
                            }
                            .padding(12)
                            .background(Color.white.opacity(0.1))
                            .cornerRadius(10)
                            .padding(.horizontal)
                            .padding(.top, 10)
                            
                            if let hero = scraper.heroItem {
                                NavigationLink(destination: DetailsView(itemId: hero.id)) {
                                    ZStack(alignment: .bottomLeading) {
                                        AsyncImage(url: URL(string: hero.imageUrl)) { image in
                                            image.resizable()
                                                 .aspectRatio(contentMode: .fill)
                                        } placeholder: {
                                            Color.gray
                                        }
                                        .frame(height: 240)
                                        .clipped()
                                        .cornerRadius(16)
                                        
                                        LinearGradient(colors: [.clear, .black.opacity(0.9)], startPoint: .top, endPoint: .bottom)
                                            .cornerRadius(16)
                                        
                                        VStack(alignment: .leading, spacing: 6) {
                                            Text("FEATURED HERO")
                                                .font(.caption2)
                                                .bold()
                                                .foregroundColor(.red)
                                                .padding(.horizontal, 8)
                                                .padding(.vertical, 4)
                                                .background(Color.black.opacity(0.6))
                                                .cornerRadius(4)
                                            
                                            Text(hero.title)
                                                .font(.title2)
                                                .bold()
                                                .foregroundColor(.white)
                                        }
                                        .padding()
                                    }
                                    .padding(.horizontal)
                                }
                            }
                            
                            ForEach(scraper.categories.keys.sorted(), id: \\.self) { categoryName in
                                VStack(alignment: .leading, spacing: 10) {
                                    Text(categoryName)
                                        .font(.title3)
                                        .bold()
                                        .foregroundColor(.white)
                                        .padding(.horizontal)
                                    
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 14) {
                                            ForEach(scraper.categories[categoryName] ?? [], id: \\.self) { item in
                                                NavigationLink(destination: DetailsView(itemId: item.id)) {
                                                    VStack(alignment: .leading) {
                                                        AsyncImage(url: URL(string: item.imageUrl)) { image in
                                                            image.resizable()
                                                                 .aspectRatio(contentMode: .fill)
                                                        } placeholder: {
                                                            Color.gray
                                                        }
                                                        .frame(width: 130, height: 190)
                                                        .clipped()
                                                        .cornerRadius(10)
                                                        
                                                        Text(item.title)
                                                            .font(.caption)
                                                            .bold()
                                                            .foregroundColor(.white)
                                                            .lineLimit(2)
                                                            .frame(width: 130, alignment: .leading)
                                                    }
                                                }
                                            }
                                        }
                                        .padding(.horizontal)
                                    }
                                }
                            }
                        }
                        .padding(.bottom, 30)
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

struct DetailsView: View {
    let itemId: String
    @StateObject private var scraper = MovieScraper()
    @State private var details: MediaDetails?
    @State private var loadingDetails = true
    
    var body: some View {
        ZStack {
            Color(red: 0.08, green: 0.09, blue: 0.12).ignoresSafeArea()
            
            if loadingDetails {
                ProgressView("Fetching Video Data Elements...")
                    .progressViewStyle(CircularProgressViewStyle(tint: .red))
                    .foregroundColor(.white)
            } else if let details = details {
                ScrollView {
                    VStack(alignment: .leading, spacing: 16) {
                        ZStack(alignment: .bottomLeading) {
                            AsyncImage(url: URL(string: details.imageUrl)) { image in
                                image.resizable()
                                     .aspectRatio(contentMode: .fill)
                            } placeholder: {
                                Color.gray
                            }
                            .frame(height: 300)
                            .clipped()
                            
                            LinearGradient(colors: [.clear, Color(red: 0.08, green: 0.09, blue: 0.12)], startPoint: .top, endPoint: .bottom)
                            
                            HStack(alignment: .bottom, spacing: 16) {
                                AsyncImage(url: URL(string: details.imageUrl)) { image in
                                    image.resizable()
                                         .aspectRatio(contentMode: .fill)
                                } placeholder: {
                                    Color.gray
                                }
                                .frame(width: 110, height: 160)
                                .clipped()
                                .cornerRadius(8)
                                
                                VStack(alignment: .leading, spacing: 8) {
                                    Text(details.title)
                                        .font(.title2)
                                        .bold()
                                        .foregroundColor(.white)
                                    
                                    HStack(spacing: 12) {
                                        Text(details.year)
                                            .font(.caption)
                                            .bold()
                                            .padding(.horizontal, 8)
                                            .padding(.vertical, 4)
                                            .background(Color.white.opacity(0.2))
                                            .cornerRadius(4)
                                            .foregroundColor(.white)
                                        
                                        HStack(spacing: 2) {
                                            Image(systemName: "star.fill")
                                                .foregroundColor(.yellow)
                                            Text(details.rating)
                                                .font(.caption)
                                                .foregroundColor(.white)
                                        }
                                    }
                                }
                            }
                            .padding()
                        }
                        
                        VStack(alignment: .leading, spacing: 8) {
                            Text("Synopsis")
                                .font(.headline)
                                .foregroundColor(.red)
                            
                            Text(details.synopsis.isEmpty ? "No internal description available." : details.synopsis)
                                .font(.body)
                                .foregroundColor(.white.opacity(0.8))
                        }
                        .padding(.horizontal)
                        
                        if !details.genre.isEmpty {
                            Text("Genres: \\(details.genre)")
                                .font(.footnote)
                                .foregroundColor(.gray)
                                .padding(.horizontal)
                        }
                        
                        Divider().background(Color.white.opacity(0.2)).padding(.horizontal)
                        
                        if details.isMovie {
                            NavigationLink(destination: CustomPlayerView(videoUrl: details.movieUrl, subtitleUrl: details.movieSubtitleUrl)) {
                                HStack {
                                    Image(systemName: "play.fill")
                                    Text("Watch Full Movie")
                                        .bold()
                                }
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(Color.red)
                                .foregroundColor(.white)
                                .cornerRadius(12)
                                .padding(.horizontal)
                            }
                        } else {
                            Text("Seasons & Episodes Layout")
                                .font(.headline)
                                .foregroundColor(.white)
                                .padding(.horizontal)
                            
                            LazyVStack(spacing: 10) {
                                ForEach(details.episodes) { episode in
                                    NavigationLink(destination: CustomPlayerView(videoUrl: episode.url, subtitleUrl: episode.subtitleUrl)) {
                                        HStack {
                                            Image(systemName: "play.circle.fill")
                                                .foregroundColor(.red)
                                                .font(.title2)
                                            
                                            VStack(alignment: .leading, spacing: 4) {
                                                Text(episode.title)
                                                    .foregroundColor(.white)
                                                    .bold()
                                                    .font(.subheadline)
                                            }
                                            Spacer()
                                            Image(systemName: "chevron.right")
                                                .foregroundColor(.gray)
                                        }
                                        .padding()
                                        .background(Color.white.opacity(0.05))
                                        .cornerRadius(8)
                                    }
                                }
                            }
                            .padding(.horizontal)
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
"""

with open("UTan/UTan/Views.swift", "w", encoding="utf-8") as f:
    f.write(views_swift)

print("Project UTan setup successfully generated without any code omissions.")
