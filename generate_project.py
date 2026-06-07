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
                self.allItemsPool = items
                if !items.isEmpty {
                    self.heroItem = items.first
                    self.categories["Trending Now"] = Array(items.prefix(min(items.count, 8)))
                    if items.count > 8 {
                        self.categories["Netflix Originals Clone"] = Array(items.dropFirst(2).prefix(8))
                        self.categories["Action & Sci-Fi Anime"] = Array(items.suffix(min(items.count - 8, 12)))
                    } else {
                        self.categories["Popular Releases"] = items
                    }
                }
            }
        }.resume()
    }
    
    func fetchDetails(id: String, completion: @escaping (MediaDetails) -> Void) {
        guard let url = URL(string: baseUrl + "index.php?do=view&type=post&id=\(id)") else { return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            var details = MediaDetails()
            details.title = "UTan Premium Screen"
            
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

enum VideoFitMode: String, CaseIterable, Identifiable {
    case fit = "Fit (MX)"
    case fill = "Stretch Fill"
    case zoom = "16:9 Crop"
    
    var id: String { self.rawValue }
    
    var gravity: AVLayerVideoGravity {
        switch self {
        case .fit: return .resizeAspect
        case .fill: return .resize
        case .zoom: return .resizeAspectFill
        }
    }
}

struct VideoPlayerRepresentable: UIViewControllerRepresentable {
    let player: AVPlayer
    let gravity: AVLayerVideoGravity
    
    func makeUIViewController(context: Context) -> AVPlayerViewController {
        let controller = AVPlayerViewController()
        controller.player = player
        controller.showsPlaybackControls = false
        controller.videoGravity = gravity
        return controller
    }
    
    func updateUIViewController(_ uiViewController: AVPlayerViewController, context: Context) {
        uiViewController.videoGravity = gravity
    }
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
    @State private var isLocked = false
    @State private var fitMode: VideoFitMode = .fit
    @State private var playbackSpeed: Double = 1.0
    @State private var showSettings = false
    
    @State private var fontSize: CGFloat = 22
    @State private var verticalOffset: CGFloat = 50
    @State private var timeObserver: Any?
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            if let player = player {
                VideoPlayerRepresentable(player: player, gravity: fitMode.gravity)
                    .ignoresSafeArea()
                    .gesture(
                        DragGesture(minimumDistance: 0)
                            .onChanged { _ in
                                if !isLocked {
                                    self.isSpeedUpActive = true
                                    player.rate = Float(2.0)
                                }
                            }
                            .onEnded { _ in
                                if !isLocked {
                                    self.isSpeedUpActive = false
                                    player.rate = Float(self.isPlaying ? playbackSpeed : 0.0)
                                }
                            }
                    )
                
                if !activeSubtitleText.isEmpty {
                    VStack {
                        Spacer()
                        Text(activeSubtitleText)
                            .font(.system(size: fontSize, weight: .bold, design: .rounded))
                            .foregroundColor(.yellow)
                            .shadow(color: .black, radius: 5, x: 2, y: 2)
                            .padding(.horizontal, 16)
                            .padding(.vertical, 8)
                            .background(Color.black.opacity(0.65))
                            .cornerRadius(10)
                            .multilineTextAlignment(.center)
                            .padding(.bottom, verticalOffset)
                    }
                    .padding(.horizontal, 30)
                    .allowsHitTesting(false)
                }
                
                if isSpeedUpActive {
                    VStack {
                        HStack(spacing: 6) {
                            Image(systemName: "forward.frame.fill")
                            Text("2.0X Fast Forward")
                                .fontWeight(.bold)
                        }
                        .font(.caption)
                        .foregroundColor(.white)
                        .padding(.horizontal, 16)
                        .padding(.vertical, 8)
                        .background(Color(red: 0.89, green: 0.04, blue: 0.08).opacity(0.85))
                        .cornerRadius(20)
                        .padding(.top, 30)
                        Spacer()
                    }
                }
                
                VStack {
                    HStack {
                        if !isLocked {
                            Button(action: {
                                shutdownPlayer()
                                presentationMode.wrappedValue.dismiss()
                            }) {
                                Image(systemName: "arrow.backward")
                                    .font(.title2)
                                    .foregroundColor(.white)
                                    .padding(12)
                                    .background(Color.black.opacity(0.5))
                                    .clipShape(Circle())
                            }
                        }
                        
                        Spacer()
                        
                        Button(action: { isLocked.toggle() }) {
                            Image(systemName: isLocked ? "lock.fill" : "lock.open.fill")
                                .font(.title2)
                                .foregroundColor(isLocked ? .red : .white)
                                .padding(12)
                                .background(Color.black.opacity(0.5))
                                .clipShape(Circle())
                        }
                        
                        if !isLocked {
                            Button(action: {
                                if fitMode == .fit { fitMode = .fill }
                                else if fitMode == .fill { fitMode = .zoom }
                                else { fitMode = .fit }
                            }) {
                                Image(systemName: "aspectratio.fill")
                                    .font(.title2)
                                    .foregroundColor(.white)
                                    .padding(12)
                                    .background(Color.black.opacity(0.5))
                                    .clipShape(Circle())
                            }
                            
                            Button(action: { showSettings.toggle() }) {
                                Image(systemName: "gearshape.fill")
                                    .font(.title2)
                                    .foregroundColor(.white)
                                    .padding(12)
                                    .background(Color.black.opacity(0.5))
                                    .clipShape(Circle())
                            }
                        }
                    }
                    .padding(.horizontal)
                    .padding(.top, 20)
                    
                    Spacer()
                    
                    if !isLocked {
                        VStack(spacing: 15) {
                            HStack {
                                Text(formatTime(currentTime))
                                    .font(.caption)
                                    .monospacedDigit()
                                    .foregroundColor(.white)
                                
                                Slider(value: $currentTime, in: 0...max(duration, 1), onEditingChanged: { editing in
                                    if !editing {
                                        player.seek(to: CMTime(seconds: currentTime, preferredTimescale: 600))
                                    }
                                })
                                .accentColor(Color(red: 0.89, green: 0.04, blue: 0.08))
                                
                                Text(formatTime(duration))
                                    .font(.caption)
                                    .monospacedDigit()
                                    .foregroundColor(.white)
                            }
                            .padding(.horizontal)
                            
                            HStack(spacing: 50) {
                                Button(action: {
                                    player.seek(to: CMTime(seconds: max(0, currentTime - 10), preferredTimescale: 600))
                                }) {
                                    Image(systemName: "gobackward.10")
                                        .font(.title)
                                        .foregroundColor(.white)
                                }
                                
                                Button(action: {
                                    if isPlaying {
                                        player.pause()
                                    } else {
                                        player.play()
                                        player.rate = Float(playbackSpeed)
                                    }
                                    isPlaying.toggle()
                                }) {
                                    Image(systemName: isPlaying ? "pause.circle.fill" : "play.circle.fill")
                                        .font(.system(size: 60))
                                        .foregroundColor(.white)
                                }
                                
                                Button(action: {
                                    player.seek(to: CMTime(seconds: min(duration, currentTime + 10), preferredTimescale: 600))
                                }) {
                                    Image(systemName: "goforward.10")
                                        .font(.title)
                                        .foregroundColor(.white)
                                }
                            }
                            .padding(.bottom, 25)
                        }
                        .background(
                            LinearGradient(colors: [.clear, .black.opacity(0.85)], startPoint: .top, endPoint: .bottom)
                        )
                    }
                }
            }
        }
        .statusBar(hidden: true)
        .onAppear {
            setupPlayer()
        }
        .onDisappear {
            shutdownPlayer()
        }
        .sheet(isPresented: $showSettings) {
            MXSettingsView(fontSize: $fontSize, verticalOffset: $verticalOffset, playbackSpeed: $playbackSpeed, player: player)
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
        
        Task {
            if let dur = try? await playerItem.asset.load(.duration) {
                DispatchQueue.main.async {
                    self.duration = dur.seconds
                }
            }
        }
        
        self.timeObserver = newPlayer.addPeriodicTimeObserver(forInterval: CMTime(seconds: 0.2, preferredTimescale: 600), queue: .main) { time in
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
    
    private func shutdownPlayer() {
        if let observer = timeObserver {
            player?.removeTimeObserver(observer)
            timeObserver = nil
        }
        player?.pause()
        player = nil
    }
    
    private func formatTime(_ seconds: TimeInterval) -> String {
        let hrs = Int(seconds) / 3600
        let mins = (Int(seconds) % 3600) / 60
        let secs = Int(seconds) % 60
        if hrs > 0 {
            return String(format: "%02d:%02d:%02d", hrs, mins, secs)
        }
        return String(format: "%02d:%02d", mins, secs)
    }
}

struct MXSettingsView: View {
    @Binding var fontSize: CGFloat
    @Binding var verticalOffset: CGFloat
    @Binding var playbackSpeed: Double
    var player: AVPlayer?
    
    @Environment(\\.presentationMode) var presentationMode
    let speeds = [0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0]
    
    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("MX Audio Speed / سرعة الفيديو")) {
                    Picker("Speed Factor", selection: $playbackSpeed) {
                        ForEach(speeds, id: \\.self) { speed in
                            Text(String(format: "%.2fx", speed)).tag(speed)
                        }
                    }
                    .pickerStyle(SegmentedPickerStyle())
                    .onChange(of: playbackSpeed) { newValue in
                        player?.rate = Float(newValue)
                    }
                }
                
                Section(header: Text("Subtitle Sizing / حجم الترجمة")) {
                    Slider(value: $fontSize, in: 16...36, step: 1)
                    Text("Font Size: \\(Int(fontSize)) pt").font(.caption).foregroundColor(.gray)
                }
                
                Section(header: Text("Vertical Padding / الارتفاع من الأسفل")) {
                    Slider(value: $verticalOffset, in: 20...160, step: 5)
                    Text("Y-Offset: \\(Int(verticalOffset)) px").font(.caption).foregroundColor(.gray)
                }
            }
            .navigationTitle("MX Engine Settings")
            .navigationBarItems(trailing: Button("Apply") {
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
                .fontWeight(.bold)
                .foregroundColor(.white)
                .opacity(0.8)
        }
    }
}

struct ContentView: View {
    @StateObject private var scraper = MovieScraper()
    @State private var searchText = ""
    
    var filteredItems: [VideoItem] {
        if searchText.isEmpty { return [] }
        return scraper.allItemsPool.filter { $0.title.localizedCaseInsensitiveContains(searchText) }
    }
    
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
                            }
                            .padding(.horizontal)
                            .padding(.top, 12)
                            
                            // Sleek Search Bar
                            HStack {
                                Image(systemName: "magnifyingglass")
                                    .foregroundColor(.gray)
                                TextField("Search global database...", text: $searchText)
                                    .foregroundColor(.white)
                                    .submitLabel(.search)
                                if !searchText.isEmpty {
                                    Button(action: { searchText = "" }) {
                                        Image(systemName: "xmark.circle.fill").foregroundColor(.gray)
                                    }
                                }
                            }
                            .padding(14)
                            .background(Color(white: 0.12))
                            .cornerRadius(12)
                            .padding(.horizontal)
                            
                            if !searchText.isEmpty {
                                Text("Search Results")
                                    .font(.title3)
                                    .fontWeight(.bold)
                                    .foregroundColor(.white)
                                    .padding(.horizontal)
                                
                                if filteredItems.isEmpty {
                                    Text("No titles matched your query.")
                                        .foregroundColor(.gray)
                                        .padding()
                                } else {
                                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 110), spacing: 15)], spacing: 20) {
                                        ForEach(filteredItems) { item in
                                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                                PremiumPosterCard(item: item)
                                            }
                                        }
                                    }
                                    .padding(.horizontal)
                                }
                            } else {
                                // Netflix Hero Showcase Banner
                                if let hero = scraper.heroItem {
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
                                                    .font(.title)
                                                    .fontWeight(.bold)
                                                    .foregroundColor(.white)
                                                    .multilineTextAlignment(.center)
                                                    .padding(.horizontal)
                                                
                                                HStack(spacing: 20) {
                                                    HStack {
                                                        Image(systemName: "play.fill")
                                                        Text("Play Now")
                                                    }
                                                    .fontWeight(.bold)
                                                    .padding(.horizontal, 24)
                                                    .padding(.vertical, 10)
                                                    .background(Color.white)
                                                    .foregroundColor(.black)
                                                    .cornerRadius(6)
                                                }
                                            }
                                            .padding(.bottom, 25)
                                        }
                                    }
                                    .cornerRadius(16)
                                    .padding(.horizontal)
                                }
                                
                                // Category Section Headers & View All Integration
                                ForEach(scraper.categories.keys.sorted(), id: \\.self) { catName in
                                    VStack(alignment: .leading, spacing: 12) {
                                        HStack {
                                            Text(catName)
                                                .font(.title3)
                                                .fontWeight(.bold)
                                                .foregroundColor(.white)
                                            Spacer()
                                            NavigationLink(destination: AllCategoryGrid(title: catName, items: scraper.categories[catName] ?? [])) {
                                                Text("View All")
                                                    .font(.footnote)
                                                    .foregroundColor(Color(red: 0.89, green: 0.04, blue: 0.08))
                                                    .fontWeight(.bold)
                                            }
                                        }
                                        .padding(.horizontal)
                                        
                                        ScrollView(.horizontal, showsIndicators: false) {
                                            HStack(spacing: 15) {
                                                ForEach(scraper.categories[catName] ?? [], id: \\.self) { item in
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
            .shadow(radius: 4)
            
            Text(item.title)
                .font(.caption)
                .fontWeight(.bold)
                .foregroundColor(.white)
                .lineLimit(1)
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
                        .font(.largeTitle)
                        .fontWeight(.bold)
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
                            .frame(height: 320)
                            .clipped()
                            
                            LinearGradient(colors: [.clear, .black.opacity(0.8), .black], startPoint: .top, endPoint: .bottom)
                            
                            HStack(alignment: .bottom, spacing: 16) {
                                AsyncImage(url: URL(string: details.imageUrl)) { image in
                                    image.resizable().aspectRatio(contentMode: .fill)
                                } placeholder: {
                                    Color(white: 0.1)
                                }
                                .frame(width: 110, height: 165)
                                .clipped()
                                .cornerRadius(8)
                                .shadow(radius: 5)
                                
                                VStack(alignment: .leading, spacing: 8) {
                                    Text(details.title)
                                        .font(.title3)
                                        .fontWeight(.bold)
                                        .foregroundColor(.white)
                                    
                                    HStack(spacing: 12) {
                                        Text(details.year)
                                            .font(.caption)
                                            .fontWeight(.bold)
                                            .padding(.horizontal, 8)
                                            .padding(.vertical, 4)
                                            .background(Color.white.opacity(0.15))
                                            .cornerRadius(4)
                                            .foregroundColor(.white)
                                        
                                        HStack(spacing: 2) {
                                            Image(systemName: "star.fill").foregroundColor(.yellow)
                                            Text(details.rating).font(.caption).foregroundColor(.white).fontWeight(.bold)
                                        }
                                    }
                                }
                            }
                            .padding()
                        }
                        
                        VStack(alignment: .leading, spacing: 10) {
                            Text("Synopsis")
                                .font(.headline)
                                .foregroundColor(Color(red: 0.89, green: 0.04, blue: 0.08))
                            
                            Text(details.synopsis.isEmpty ? "No platform overview summary is written yet." : details.synopsis)
                                .font(.body)
                                .foregroundColor(.white.opacity(0.85))
                                .lineSpacing(4)
                        }
                        .padding(.horizontal)
                        
                        if details.isMovie {
                            NavigationLink(destination: CustomPlayerView(videoUrl: details.movieUrl, subtitleUrl: details.movieSubtitleUrl)) {
                                HStack {
                                    Image(systemName: "play.fill")
                                    Text("Stream Feature Movie")
                                        .fontWeight(.bold)
                                }
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(Color(red: 0.89, green: 0.04, blue: 0.08))
                                .foregroundColor(.white)
                                .cornerRadius(8)
                                .padding(.horizontal)
                            }
                        } else {
                            Text("Episodes List")
                                .font(.headline)
                                .foregroundColor(.white)
                                .padding(.horizontal)
                            
                            LazyVStack(spacing: 12) {
                                ForEach(details.episodes) { episode in
                                    NavigationLink(destination: CustomPlayerView(videoUrl: episode.url, subtitleUrl: episode.subtitleUrl)) {
                                        HStack {
                                            Image(systemName: "play.rectangle.fill")
                                                .foregroundColor(Color(red: 0.89, green: 0.04, blue: 0.08))
                                                .font(.title3)
                                            
                                            Text(episode.title)
                                                .foregroundColor(.white)
                                                .fontWeight(.bold)
                                                .font(.subheadline)
                                            Spacer()
                                            Image(systemName: "chevron.right").foregroundColor(.gray).font(.caption)
                                        }
                                        .padding()
                                        .background(Color(white: 0.1))
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

print("Project UTan PREMIUM setup successfully generated without any code omissions.")
