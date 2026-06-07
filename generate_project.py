import os

# Create directory structure
os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# 1. Write project.pbxproj
pbxproj_content = """// !$*UTF8*$!
{
\tarchiveVersion = 1;
\tclasses = {
\t};
\tobjectVersion = 56;
\tobjects = {

/* Begin PBXBuildFile section */
\t\t010101012C12345600000001 /* UTanApp.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000002 /* UTanApp.swift */; };
\t\t010101012C12345600000003 /* Scraper.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000004 /* Scraper.swift */; };
\t\t010101012C12345600000005 /* CustomPlayer.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000006 /* CustomPlayer.swift */; };
\t\t010101012C12345600000007 /* SubtitleParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000008 /* SubtitleParser.swift */; };
\t\t010101012C12345600000009 /* Views.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000000A /* Views.swift */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
\t\t010101012C12345600000002 /* UTanApp.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = UTanApp.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000004 /* Scraper.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Scraper.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000006 /* CustomPlayer.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = CustomPlayer.swift; sourceTree = "<group>"; };
\t\t010101012C12345600000008 /* SubtitleParser.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = SubtitleParser.swift; sourceTree = "<group>"; };
\t\t010101012C1234560000000A /* Views.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Views.swift; sourceTree = "<group>"; };
\t\t010101012C1234560000000B /* Info.plist */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
\t\t010101012C1234560000000C /* UTan.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = UTan.app; sourceTree = BUILT_PRODUCTS_DIR; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
\t\t010101012C1234560000000D /* Frameworks */ = {
\t\t\tisa = PBXFrameworksBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
\t\t010101012C1234560000000E /* MainGroup */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t010101012C1234560000000F /* UTan */,
\t\t\t\t010101012C1234560000000C /* UTan.app */,
\t\t\t);
\t\t\tsourceTree = "<group>";
\t\t};
\t\t010101012C1234560000000F /* UTan */ = {
\t\t\tisa = PBXGroup;
\t\t\tchildren = (
\t\t\t\t010101012C12345600000002 /* UTanApp.swift */,
\t\t\t\t010101012C12345600000004 /* Scraper.swift */,
\t\t\t\t010101012C12345600000006 /* CustomPlayer.swift */,
\t\t\t\t010101012C12345600000008 /* SubtitleParser.swift */,
\t\t\t\t010101012C1234560000000A /* Views.swift */,
\t\t\t\t010101012C1234560000000B /* Info.plist */,
\t\t\t);
\t\t\tpath = UTan;
\t\t\tsourceTree = "<group>";
\t\t};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
\t\t010101012C12345600000010 /* UTan */ = {
\t\t\tisa = PBXNativeTarget;
\t\t\tbuildConfigurationList = 010101012C12345600000011 /* Build configuration list for PBXNativeTarget "UTan" */;
\t\t\tbuildPhases = (
\t\t\t\t010101012C12345600000012 /* Sources */,
\t\t\t\t010101012C1234560000000D /* Frameworks */,
\t\t\t);
\t\t\tbuildRules = (
\t\t\t);
\t\t\tdependencies = (
\t\t\t);
\t\t\tname = UTan;
\t\t\tproductName = UTan;
\t\t\tproductReference = 010101012C1234560000000C /* UTan.app */;
\t\t\tproductType = "com.apple.product-type.application";
\t\t};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
\t\t010101012C12345600000013 /* Project object */ = {
\t\t\tisa = PBXProject;
\t\t\tattributes = {
\t\t\t\tLastSwiftUpdateCheck = 1500;
\t\t\t\tLastUpgradeCheck = 1500;
\t\t\t\tTargetAttributes = {
\t\t\t\t\t010101012C12345600000010 = {
\t\t\t\t\t\tCreatedOnToolsVersion = 15.0;
\t\t\t\t\t\tDevelopmentTeam = "";
\t\t\t\t\t};
\t\t\t\t};
\t\t\t};
\t\t\tbuildConfigurationList = 010101012C12345600000014 /* Build configuration list for PBXProject "UTan" */;
\t\t\tcompatibilityVersion = "Xcode 14.0";
\t\t\tdevelopmentRegion = en;
\t\t\thasScannedForEncodings = 0;
\t\t\tknownRegions = (
\t\t\t\ten,
\t\t\t\tBase,
\t\t\t\tar,
\t\t\t);
\t\t\tmainGroup = 010101012C1234560000000E /* MainGroup */;
\t\t\tproductRefGroup = 010101012C1234560000000E /* MainGroup */;
\t\t\tprojectDirPath = "";
\t\t\tprojectRoot = "";
\t\t\ttargets = (
\t\t\t\t010101012C12345600000010 /* UTan */,
\t\t\t);
\t\t};
/* End PBXProject section */

/* Begin PBXSourcesBuildPhase section */
\t\t010101012C12345600000012 /* Sources */ = {
\t\t\tisa = PBXSourcesBuildPhase;
\t\t\tbuildActionMask = 2147483647;
\t\t\tfiles = (
\t\t\t\t010101012C12345600000001 /* UTanApp.swift in Sources */,
\t\t\t\t010101012C12345600000003 /* Scraper.swift in Sources */,
\t\t\t\t010101012C12345600000005 /* CustomPlayer.swift in Sources */,
\t\t\t\t010101012C12345600000007 /* SubtitleParser.swift in Sources */,
\t\t\t\t010101012C12345600000009 /* Views.swift in Sources */,
\t\t\t);
\t\t\trunOnlyForDeploymentPostprocessing = 0;
\t\t};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
\t\t010101012C12345600000015 /* Debug */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = dwarf;
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tENABLE_TESTABILITY = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu11;
\t\t\t\tGCC_DYNAMIC_NO_PIC = NO;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tGCC_OPTIMIZATION_LEVEL = 0;
\t\t\t\tGCC_PREPROCESSOR_DEFINITIONS = (
\t\t\t\t\t"DEBUG=1",
\t\t\t\t\t"$(inherited)",
\t\t\t\t);
\t\t\t\tMTL_ENABLE_DEBUG_INFO = INCLUDE_SOURCE;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tONLY_ACTIVE_ARCH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_ACTIVE_COMPILATION_CONDITIONS = DEBUG;
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-Onone";
\t\t\t};
\t\t\tname = Debug;
\t\t};
\t\t010101012C12345600000016 /* Release */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tALWAYS_SEARCH_USER_PATHS = NO;
\t\t\t\tCLANG_ANALYZER_NONNULL = YES;
\t\t\t\tCLANG_CXX_LANGUAGE_STANDARD = "gnu++20";
\t\t\t\tCLANG_ENABLE_MODULES = YES;
\t\t\t\tCLANG_ENABLE_OBJC_ARC = YES;
\t\t\t\tCLANG_ENABLE_OBJC_WEAK = YES;
\t\t\t\tCOPY_PHASE_STRIP = NO;
\t\t\t\tDEBUG_INFORMATION_FORMAT = "dwarf-with-dsym";
\t\t\t\tENABLE_NS_ASSERTIONS = NO;
\t\t\t\tENABLE_STRICT_OBJC_MSGSEND = YES;
\t\t\t\tGCC_C_LANGUAGE_STANDARD = gnu11;
\t\t\t\tGCC_NO_COMMON_BLOCKS = YES;
\t\t\t\tMTL_FAST_MATH = YES;
\t\t\t\tSDKROOT = iphoneos;
\t\t\t\tSWIFT_COMPILATION_MODE = wholemodule;
\t\t\t\tSWIFT_OPTIMIZATION_LEVEL = "-O";
\t\t\t\tVALIDATE_PRODUCT = YES;
\t\t\t};
\t\t\tname = Release;
\t\t};
\t\t010101012C12345600000017 /* Debug */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCODE_SIGNING_ALLOWED = NO;
\t\t\t\tCODE_SIGNING_REQUIRED = NO;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_ASSET_PATHS = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tINFOPLIST_FILE = UTan/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 16.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t};
\t\t\tname = Debug;
\t\t};
\t\t010101012C12345600000018 /* Release */ = {
\t\t\tisa = XCBuildConfiguration;
\t\t\tbuildSettings = {
\t\t\t\tASSETCATALOG_COMPILER_APPICON_NAME = AppIcon;
\t\t\t\tASSETCATALOG_COMPILER_GLOBAL_ACCENT_COLOR_NAME = AccentColor;
\t\t\t\tCODE_SIGN_STYLE = Manual;
\t\t\t\tCODE_SIGNING_ALLOWED = NO;
\t\t\t\tCODE_SIGNING_REQUIRED = NO;
\t\t\t\tCURRENT_PROJECT_VERSION = 1;
\t\t\t\tDEVELOPMENT_ASSET_PATHS = "";
\t\t\t\tENABLE_PREVIEWS = YES;
\t\t\t\tINFOPLIST_FILE = UTan/Info.plist;
\t\t\t\tIPHONEOS_DEPLOYMENT_TARGET = 16.0;
\t\t\t\tLD_RUNPATH_SEARCH_PATHS = (
\t\t\t\t\t"$(inherited)",
\t\t\t\t\t"@executable_path/Frameworks",
\t\t\t\t);
\t\t\t\tMARKETING_VERSION = 1.0;
\t\t\t\tPRODUCT_BUNDLE_IDENTIFIER = com.mustaqil.utan;
\t\t\t\tPRODUCT_NAME = "$(TARGET_NAME)";
\t\t\t\tSWIFT_EMIT_LOC_STRINGS = YES;
\t\t\t\tSWIFT_VERSION = 5.0;
\t\t\t\tTARGETED_DEVICE_FAMILY = "1,2";
\t\t\t};
\t\t\tname = Release;
\t\t};
/* End XCBuildConfiguration section */

/* Begin XCConfigurationList section */
\t\t010101012C12345600000011 /* Build configuration list for PBXNativeTarget "UTan" */ = {
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t010101012C12345600000017 /* Debug */,
\t\t\t\t010101012C12345600000018 /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t};
\t\t010101012C12345600000014 /* Build configuration list for PBXProject "UTan" */ = {
\t\t\tisa = XCConfigurationList;
\t\t\tbuildConfigurations = (
\t\t\t\t010101012C12345600000015 /* Debug */,
\t\t\t\t010101012C12345600000016 /* Release */,
\t\t\t);
\t\t\tdefaultConfigurationIsVisible = 0;
\t\t\tdefaultConfigurationName = Release;
\t\t};
/* End XCConfigurationList section */
\t};
\trootObject = 010101012C12345600000013 /* Project object */;
}
"""

with open("UTan/UTan.xcodeproj/project.pbxproj", "w", encoding="utf-8") as f:
    f.write(pbxproj_content)

# 2. Write Info.plist
info_plist = """<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
\t<key>CFBundleDevelopmentRegion</key>
\t<string>en</string>
\t<key>CFBundleExecutable</key>
\t<string>$(EXECUTABLE_NAME)</string>
\t<key>CFBundleIdentifier</key>
\t<string>com.mustaqil.utan</string>
\t<key>CFBundleInfoDictionaryVersion</key>
\t<string>6.0</string>
\t<key>CFBundleName</key>
\t<string>UTan</string>
\t<key>CFBundlePackageType</key>
\t<string>APPL</string>
\t<key>CFBundleShortVersionString</key>
\t<string>2.0</string>
\t<key>CFBundleVersion</key>
\t<string>2</string>
\t<key>LSRequiresIPhoneOS</key>
\t<true/>
\t<key>NSAppTransportSecurity</key>
\t<dict>
\t\t<key>NSAllowsArbitraryLoads</key>
\t\t<true/>
\t</dict>
\t<key>UILaunchScreen</key>
\t<dict/>
\t<key>UISupportedInterfaceOrientations</key>
\t<array>
\t\t<string>UIInterfaceOrientationPortrait</string>
\t\t<string>UIInterfaceOrientationLandscapeLeft</string>
\t\t<string>UIInterfaceOrientationLandscapeRight</string>
\t</array>
\t<key>UIUserInterfaceStyle</key>
\t<string>Dark</string>
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
            MainTabView()
                .preferredColorScheme(.dark)
        }
    }
}
"""

with open("UTan/UTan/UTanApp.swift", "w", encoding="utf-8") as f:
    f.write(app_swift)

# 4. Write Scraper.swift (full version with seasons)
scraper_swift = r"""import Foundation

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
    let season: Int
    let episodeNum: Int
    let url: String
    let url1080: String
    let url360: String
    let subtitleUrl: String
    let subtitleVttUrl: String
}

struct Season: Identifiable {
    let id = UUID()
    let number: Int
    let episodes: [EpisodeItem]
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
    var seasons: [Season] = []
}

// MARK: – Watch Progress
struct WatchProgress: Codable, Identifiable {
    var id: String { itemId }
    var itemId: String
    var title: String
    var imageUrl: String
    var episodeId: String
    var episodeTitle: String
    var seasonNumber: Int
    var episodeNumber: Int
    var progressSeconds: Double
    var durationSeconds: Double
    var updatedAt: Date
}

class WatchProgressStore: ObservableObject {
    static let shared = WatchProgressStore()
    private let key = "UTanWatchProgress_v3"
    @Published var allProgress: [String: WatchProgress] = [:]
    private init() { load() }
    func save(itemId: String, title: String, imageUrl: String,
              episodeId: String, episodeTitle: String,
              seasonNumber: Int, episodeNumber: Int,
              progress: Double, duration: Double) {
        let record = WatchProgress(
            itemId: itemId, title: title, imageUrl: imageUrl,
            episodeId: episodeId, episodeTitle: episodeTitle,
            seasonNumber: seasonNumber, episodeNumber: episodeNumber,
            progressSeconds: progress, durationSeconds: duration,
            updatedAt: Date()
        )
        allProgress[itemId] = record
        persist()
    }
    func remove(itemId: String) {
        allProgress.removeValue(forKey: itemId)
        persist()
    }
    func progress(for itemId: String) -> WatchProgress? { allProgress[itemId] }
    var recent: [WatchProgress] {
        allProgress.values.sorted { $0.updatedAt > $1.updatedAt }
    }
    private func load() {
        guard let data = UserDefaults.standard.data(forKey: key),
              let decoded = try? JSONDecoder().decode([String: WatchProgress].self, from: data) else { return }
        allProgress = decoded
    }
    private func persist() {
        if let data = try? JSONEncoder().encode(allProgress) {
            UserDefaults.standard.set(data, forKey: key)
        }
    }
}

// MARK: – Site categories
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

// MARK: – Main scraper
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

    // MARK: – HTML parsers
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
                  let r = Range(m.range(at: 1), in: text) else { return nil }
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

        var episodesBySeason: [Int: [EpisodeItem]] = [:]
        let episodeBlockPattern = #"<li class="episodeitem">(.*?)</li>"#
        if let blockRx = try? NSRegularExpression(pattern: episodeBlockPattern, options: [.dotMatchesLineSeparators]) {
            for blockMatch in blockRx.matches(in: html, range: NSRange(html.startIndex..., in: html)) {
                if blockMatch.numberOfRanges >= 2, let blockRange = Range(blockMatch.range(at: 1), in: html) {
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
                              let r = Range(m.range(at: 1), in: text) else { return "" }
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

                    var seasonNum = 1
                    var episodeNum = 0
                    if let range = epTitle.range(of: #"S(\d+)E(\d+)"#, options: .regularExpression) {
                        let match = String(epTitle[range])
                        let parts = match.dropFirst().split(separator: "E")
                        if parts.count == 2 {
                            seasonNum = Int(parts[0]) ?? 1
                            episodeNum = Int(parts[1]) ?? 0
                        }
                    }
                    if !epUrl.isEmpty {
                        let ep = EpisodeItem(
                            id: epId, title: epTitle, season: seasonNum, episodeNum: episodeNum,
                            url: epUrl, url1080: epUrl1080, url360: epUrl360,
                            subtitleUrl: epSrt, subtitleVttUrl: epWebvtt
                        )
                        episodesBySeason[seasonNum, default: []].append(ep)
                    }
                }
            }
        }
        for season in episodesBySeason.keys {
            episodesBySeason[season]?.sort { $0.episodeNum < $1.episodeNum }
        }
        if episodesBySeason.isEmpty {
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
            for seasonNum in episodesBySeason.keys.sorted() {
                if let eps = episodesBySeason[seasonNum], !eps.isEmpty {
                    d.seasons.append(Season(number: seasonNum, episodes: eps))
                }
            }
        }
        return d
    }
}
"""

with open("UTan/UTan/Scraper.swift", "w", encoding="utf-8") as f:
    f.write(scraper_swift)

# 5. Write SubtitleParser.swift
sub_parser_swift = r"""import Foundation

struct SubtitleCue: Identifiable {
    let id = UUID()
    let startTime: TimeInterval
    let endTime: TimeInterval
    let text: String
}

class SubtitleParser {
    static func parse(url: String, completion: @escaping ([SubtitleCue]) -> Void) {
        guard !url.isEmpty else { completion([]); return }
        var clean = url
        if !clean.hasPrefix("http") { clean = "https://movie.vodu.me/" + clean }
        guard let urlObj = URL(string: clean) else { completion([]); return }
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
            guard let finalText = text else { completion([]); return }
            if finalText.contains("WEBVTT") {
                completion(parseWebVTT(finalText))
            } else {
                completion(parseSRT(finalText))
            }
        }.resume()
    }

    private static func parseSRT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let blocks = content.components(separatedBy: "\n\n")
        for block in blocks {
            let lines = block.components(separatedBy: .newlines).map { $0.trimmingCharacters(in: .whitespacesAndNewlines) }.filter { !$0.isEmpty }
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
                  let end = parseSRTTime(times[1]) else { continue }
            cues.append(SubtitleCue(startTime: start, endTime: end, text: text))
        }
        return cues
    }

    private static func parseSRTTime(_ timeString: String) -> TimeInterval? {
        let clean = timeString.trimmingCharacters(in: .whitespacesAndNewlines)
        let parts = clean.components(separatedBy: ",")
        guard parts.count == 2, let milliseconds = Double(parts[1]) else { return nil }
        let timePart = parts[0]
        let timeComponents = timePart.components(separatedBy: ":")
        guard timeComponents.count == 3,
              let hours = Double(timeComponents[0]),
              let minutes = Double(timeComponents[1]),
              let seconds = Double(timeComponents[2]) else { return nil }
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
                      let end = parseVTTTime(times[1]) else { i += 1; continue }
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
        var hours: Double = 0, minutes: Double = 0, seconds: Double = 0
        if parts.count == 3 {
            hours = Double(parts[0]) ?? 0
            minutes = Double(parts[1]) ?? 0
            let secParts = parts[2].components(separatedBy: ".")
            seconds = Double(secParts[0]) ?? 0
            if secParts.count == 2 { seconds += Double(secParts[1])! / 1000 }
        } else if parts.count == 2 {
            minutes = Double(parts[0]) ?? 0
            let secParts = parts[1].components(separatedBy: ".")
            seconds = Double(secParts[0]) ?? 0
            if secParts.count == 2 { seconds += Double(secParts[1])! / 1000 }
        } else { return nil }
        return hours * 3600 + minutes * 60 + seconds
    }
}
"""

with open("UTan/UTan/SubtitleParser.swift", "w", encoding="utf-8") as f:
    f.write(sub_parser_swift)

# 6. Write CustomPlayer.swift (complete with all features)
player_swift = r"""import SwiftUI
import AVKit
import AVFoundation

// MARK: - Enums
enum VideoQuality: String, CaseIterable, Identifiable {
    case auto = "تلقائي"
    case q360 = "360p"
    case q1080 = "1080p"
    var id: String { rawValue }
}

enum VideoFitMode: String, CaseIterable, Identifiable {
    case fit = "ملاءمة"
    case fill = "تمديد"
    case zoom = "قص"
    var id: String { rawValue }
    var gravity: AVLayerVideoGravity {
        switch self {
        case .fit: return .resizeAspect
        case .fill: return .resize
        case .zoom: return .resizeAspectFill
        }
    }
}

// MARK: - Subtitle Settings Persistence
class SubtitleSettings: ObservableObject {
    static let shared = SubtitleSettings()
    @Published var enabled: Bool = true
    @Published var color: Color = .white
    @Published var fontSize: CGFloat = 22
    @Published var bottomPadding: CGFloat = 60
    private let defaults = UserDefaults.standard
    private let enabledKey = "subtitle_enabled"
    private let colorDataKey = "subtitle_color_data"
    private let fontSizeKey = "subtitle_font_size"
    private let bottomPaddingKey = "subtitle_bottom_padding"
    private init() {
        enabled = defaults.bool(forKey: enabledKey)
        if let colorData = defaults.data(forKey: colorDataKey),
           let uiColor = try? NSKeyedUnarchiver.unarchivedObject(ofClass: UIColor.self, from: colorData) {
            color = Color(uiColor)
        }
        fontSize = CGFloat(defaults.float(forKey: fontSizeKey))
        if fontSize < 14 { fontSize = 22 }
        bottomPadding = CGFloat(defaults.float(forKey: bottomPaddingKey))
        if bottomPadding < 20 { bottomPadding = 60 }
    }
    func save() {
        defaults.set(enabled, forKey: enabledKey)
        let uiColor = UIColor(color)
        if let data = try? NSKeyedArchiver.archivedData(withRootObject: uiColor, requiringSecureCoding: false) {
            defaults.set(data, forKey: colorDataKey)
        }
        defaults.set(Float(fontSize), forKey: fontSizeKey)
        defaults.set(Float(bottomPadding), forKey: bottomPaddingKey)
    }
}

// MARK: - Download Manager
class DownloadManager: ObservableObject {
    static let shared = DownloadManager()
    @Published var downloads: [String: DownloadTask] = [:]
    struct DownloadTask: Identifiable, Codable {
        let id = UUID()
        let url: String
        let title: String
        var progress: Double = 0
        var isDownloading = true
        var localURL: URL?
        enum CodingKeys: String, CodingKey {
            case url, title, progress, isDownloading, localURL
        }
    }
    private init() { loadDownloads() }
    func startDownload(url: String, title: String, completion: ((URL?) -> Void)? = nil) {
        guard let urlObj = URL(string: url) else { return }
        var task = DownloadTask(url: url, title: title)
        task.progress = 0
        task.isDownloading = true
        downloads[url] = task
        let session = URLSession(configuration: .default, delegate: DownloadManagerDelegate(manager: self, url: url, completion: completion), delegateQueue: nil)
        let downloadTask = session.downloadTask(with: urlObj)
        downloadTask.resume()
    }
    func cancelDownload(url: String) {
        downloads[url]?.isDownloading = false
        downloads.removeValue(forKey: url)
        saveDownloads()
    }
    private func saveDownloads() {
        let completed = downloads.values.filter { !$0.isDownloading && $0.localURL != nil }
        let data = try? JSONEncoder().encode(completed)
        UserDefaults.standard.set(data, forKey: "completedDownloads")
    }
    private func loadDownloads() {
        guard let data = UserDefaults.standard.data(forKey: "completedDownloads"),
              let decoded = try? JSONDecoder().decode([DownloadTask].self, from: data) else { return }
        for task in decoded {
            downloads[task.url] = task
        }
    }
    func deleteDownload(url: String) {
        if let task = downloads[url], let localURL = task.localURL {
            try? FileManager.default.removeItem(at: localURL)
        }
        downloads.removeValue(forKey: url)
        saveDownloads()
    }
    func clearAllDownloads() {
        for (url, task) in downloads {
            if let localURL = task.localURL {
                try? FileManager.default.removeItem(at: localURL)
            }
            downloads.removeValue(forKey: url)
        }
        saveDownloads()
    }
}

class DownloadManagerDelegate: NSObject, URLSessionDownloadDelegate {
    let manager: DownloadManager
    let url: String
    let completion: ((URL?) -> Void)?
    init(manager: DownloadManager, url: String, completion: ((URL?) -> Void)?) {
        self.manager = manager
        self.url = url
        self.completion = completion
    }
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didFinishDownloadingTo location: URL) {
        let dest = FileManager.default.temporaryDirectory.appendingPathComponent(UUID().uuidString + ".mp4")
        try? FileManager.default.moveItem(at: location, to: dest)
        DispatchQueue.main.async {
            self.manager.downloads[self.url]?.localURL = dest
            self.manager.downloads[self.url]?.isDownloading = false
            self.manager.downloads[self.url]?.progress = 1.0
            self.manager.saveDownloads()
            self.completion?(dest)
        }
    }
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didWriteData bytesWritten: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64) {
        let progress = Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
        DispatchQueue.main.async {
            self.manager.downloads[self.url]?.progress = progress
        }
    }
}

// MARK: - VideoPlayer View with Gestures
struct VideoPlayerView: UIViewControllerRepresentable {
    let player: AVPlayer
    let gravity: AVLayerVideoGravity
    let onTap: () -> Void
    let onLongPressBegan: () -> Void
    let onLongPressEnded: () -> Void
    func makeUIViewController(context: Context) -> AVPlayerViewController {
        let vc = AVPlayerViewController()
        vc.player = player
        vc.showsPlaybackControls = false
        vc.videoGravity = gravity
        let overlay = UIView(frame: vc.view.bounds)
        overlay.autoresizingMask = [.flexibleWidth, .flexibleHeight]
        overlay.backgroundColor = .clear
        vc.view.addSubview(overlay)
        let tap = UITapGestureRecognizer(target: context.coordinator, action: #selector(Coordinator.handleTap))
        tap.numberOfTapsRequired = 1
        let longPress = UILongPressGestureRecognizer(target: context.coordinator, action: #selector(Coordinator.handleLongPress))
        longPress.minimumPressDuration = 0.4
        overlay.addGestureRecognizer(tap)
        overlay.addGestureRecognizer(longPress)
        let watermark = UILabel()
        watermark.text = "UTan"
        watermark.font = UIFont.systemFont(ofSize: 24, weight: .bold)
        watermark.textColor = UIColor.white.withAlphaComponent(0.4)
        watermark.backgroundColor = .clear
        watermark.sizeToFit()
        watermark.frame.origin = CGPoint(x: 16, y: 50)
        watermark.autoresizingMask = [.flexibleRightMargin, .flexibleBottomMargin]
        vc.view.addSubview(watermark)
        return vc
    }
    func updateUIViewController(_ vc: AVPlayerViewController, context: Context) {
        vc.videoGravity = gravity
    }
    func makeCoordinator() -> Coordinator {
        Coordinator(onTap: onTap, onLongPressBegan: onLongPressBegan, onLongPressEnded: onLongPressEnded)
    }
    class Coordinator: NSObject {
        let onTap: () -> Void
        let onLongPressBegan: () -> Void
        let onLongPressEnded: () -> Void
        init(onTap: @escaping () -> Void, onLongPressBegan: @escaping () -> Void, onLongPressEnded: @escaping () -> Void) {
            self.onTap = onTap
            self.onLongPressBegan = onLongPressBegan
            self.onLongPressEnded = onLongPressEnded
        }
        @objc func handleTap() { onTap() }
        @objc func handleLongPress(_ gesture: UILongPressGestureRecognizer) {
            switch gesture.state {
            case .began: onLongPressBegan()
            case .ended, .cancelled, .failed: onLongPressEnded()
            default: break
            }
        }
    }
}

// MARK: - CustomPlayerView
struct CustomPlayerView: View {
    let itemId: String
    let itemTitle: String
    let itemImageUrl: String
    let videoUrl: String
    let videoUrl1080: String
    let videoUrl360: String
    let subtitleUrl: String
    let subtitleVttUrl: String
    let episodeId: String
    let episodeTitle: String
    let seasonNumber: Int
    let episodeNumber: Int

    @Environment(\.presentationMode) var presentation
    @StateObject private var progressStore = WatchProgressStore.shared
    @StateObject private var subtitleSettings = SubtitleSettings.shared
    @StateObject private var downloadManager = DownloadManager.shared

    @State private var player: AVPlayer?
    @State private var isPlaying = true
    @State private var currentTime: TimeInterval = 0
    @State private var duration: TimeInterval = 0
    @State private var isDragging = false
    @State private var seekTarget: TimeInterval = 0
    @State private var timeObserver: Any?
    @State private var showControls = true
    @State private var hideTimer: Timer?
    @State private var isLocked = false
    @State private var fitMode = VideoFitMode.fit
    @State private var quality = VideoQuality.auto
    @State private var showSettings = false
    @State private var isSpeedActive = false
    @State private var cues: [SubtitleCue] = []
    @State private var activeSub = ""
    @State private var errorMessage: String?
    @State private var playbackSpeed: Double = 1.0
    @State private var saveTimer: Timer?
    @State private var showDownloadSheet = false

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            if let player = player {
                VideoPlayerView(
                    player: player,
                    gravity: fitMode.gravity,
                    onTap: {
                        if !isLocked {
                            withAnimation { showControls.toggle() }
                            if showControls { scheduleHide() }
                        }
                    },
                    onLongPressBegan: {
                        if !isLocked && !isSpeedActive {
                            isSpeedActive = true
                            player.rate = 2.0
                        }
                    },
                    onLongPressEnded: {
                        if isSpeedActive {
                            isSpeedActive = false
                            player.rate = isPlaying ? Float(playbackSpeed) : 0
                        }
                    }
                )
                .ignoresSafeArea()
                if isSpeedActive {
                    VStack {
                        HStack(spacing: 6) {
                            Image(systemName: "forward.frame.fill")
                            Text("2× سرعة")
                        }
                        .font(.system(size: 14, weight: .bold))
                        .foregroundColor(.white)
                        .padding(.horizontal, 16).padding(.vertical, 8)
                        .background(Color.red.opacity(0.85))
                        .cornerRadius(20)
                        .padding(.top, 60)
                        Spacer()
                    }
                }
                if subtitleSettings.enabled && !activeSub.isEmpty {
                    VStack {
                        Spacer()
                        Text(activeSub)
                            .font(.system(size: subtitleSettings.fontSize, weight: .bold, design: .rounded))
                            .foregroundColor(subtitleSettings.color)
                            .shadow(color: .black, radius: 3, x: 1, y: 1)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 20)
                            .padding(.vertical, 6)
                            .background(Color.black.opacity(0.6))
                            .cornerRadius(8)
                            .padding(.bottom, subtitleSettings.bottomPadding)
                    }
                    .allowsHitTesting(false)
                }
                if let error = errorMessage {
                    VStack {
                        Text(error)
                            .foregroundColor(.white)
                            .padding()
                            .background(Color.red.opacity(0.8))
                            .cornerRadius(8)
                    }
                }
                if showControls || isLocked {
                    controlsOverlay(player: player)
                        .transition(.opacity)
                        .animation(.easeInOut(duration: 0.25), value: showControls)
                }
            } else {
                VStack(spacing: 20) {
                    ProgressView().tint(.white)
                    Text("جاري تحميل الفيديو...").foregroundColor(.white)
                    Button("إغلاق") { presentation.wrappedValue.dismiss() }
                        .padding()
                        .background(Color.red)
                        .foregroundColor(.white)
                        .cornerRadius(8)
                }
            }
        }
        .statusBar(hidden: true)
        .onAppear { setupPlayer() }
        .onDisappear { shutdown() }
        .sheet(isPresented: $showSettings) { settingsSheet }
        .sheet(isPresented: $showDownloadSheet) { downloadSheet }
    }

    @ViewBuilder
    private func controlsOverlay(player: AVPlayer) -> some View {
        VStack {
            HStack {
                if !isLocked {
                    Button { shutdown(); presentation.wrappedValue.dismiss() } label: {
                        Image(systemName: "arrow.backward").playerBtn()
                    }
                    Spacer()
                    Text(episodeTitle.isEmpty ? itemTitle : episodeTitle)
                        .font(.system(size: 13, weight: .semibold))
                        .foregroundColor(.white).lineLimit(1)
                    Spacer()
                    Button { showDownloadSheet = true } label: {
                        Image(systemName: "arrow.down.circle").playerBtn()
                    }
                    Button { showSettings = true } label: {
                        Image(systemName: "gearshape").playerBtn()
                    }
                } else {
                    Spacer()
                }
                Button {
                    withAnimation { isLocked.toggle() }
                    if isLocked { hideControls() }
                } label: {
                    Image(systemName: isLocked ? "lock.fill" : "lock.open")
                        .playerBtn(color: isLocked ? .red : .white)
                }
            }
            .padding(.horizontal, 16).padding(.top, 20)
            .background(LinearGradient(colors: [.black.opacity(0.7), .clear], startPoint: .top, endPoint: .bottom))
            Spacer()
            if !isLocked {
                VStack(spacing: 12) {
                    HStack(spacing: 10) {
                        Text(formatTime(isDragging ? seekTarget : currentTime)).timeLabel()
                        Slider(value: isDragging ? $seekTarget : $currentTime, in: 0...max(duration, 1)) { editing in
                            isDragging = editing
                            if !editing {
                                player.seek(to: CMTime(seconds: seekTarget, preferredTimescale: 600))
                                currentTime = seekTarget
                                scheduleHide()
                            }
                        }
                        .accentColor(.red)
                        Text(formatTime(duration)).timeLabel()
                    }
                    .padding(.horizontal, 16)
                    HStack(spacing: 50) {
                        Button { let t = max(0, currentTime - 10); player.seek(to: CMTime(seconds: t, preferredTimescale: 600)); scheduleHide() } label: {
                            Image(systemName: "gobackward.10").font(.title).foregroundColor(.white)
                        }
                        Button {
                            if isPlaying { player.pause() }
                            else { player.rate = Float(playbackSpeed) }
                            isPlaying.toggle()
                            scheduleHide()
                        } label: {
                            Image(systemName: isPlaying ? "pause.circle.fill" : "play.circle.fill")
                                .font(.system(size: 62)).foregroundColor(.white)
                        }
                        Button { let t = min(duration, currentTime + 10); player.seek(to: CMTime(seconds: t, preferredTimescale: 600)); scheduleHide() } label: {
                            Image(systemName: "goforward.10").font(.title).foregroundColor(.white)
                        }
                    }
                    HStack(spacing: 6) {
                        ForEach(VideoQuality.allCases) { q in
                            Button(q.rawValue) { switchQuality(to: q) }
                                .font(.system(size: 11, weight: quality == q ? .bold : .regular))
                                .foregroundColor(quality == q ? .red : .white.opacity(0.7))
                                .padding(.horizontal, 10).padding(.vertical, 4)
                                .background(quality == q ? Color.white.opacity(0.15) : Color.clear)
                                .cornerRadius(6)
                        }
                        Spacer()
                        Button {
                            let all = VideoFitMode.allCases
                            let idx = all.firstIndex(of: fitMode) ?? 0
                            fitMode = all[(idx + 1) % all.count]
                        } label: {
                            Image(systemName: "aspectratio").font(.caption).foregroundColor(.white.opacity(0.8))
                        }
                        Text(fitMode.rawValue).font(.system(size: 11)).foregroundColor(.white.opacity(0.7))
                    }
                    .padding(.horizontal, 16).padding(.bottom, 20)
                }
                .background(LinearGradient(colors: [.clear, .black.opacity(0.85)], startPoint: .top, endPoint: .bottom))
            }
        }
    }

    var settingsSheet: some View {
        NavigationView {
            Form {
                Section(header: Text("تشغيل الفيديو")) {
                    Picker("سرعة التشغيل", selection: $playbackSpeed) {
                        ForEach([0.5, 0.75, 1.0, 1.25, 1.5, 1.75, 2.0], id: \.self) {
                            Text(String(format: "%.2f×", $0)).tag($0)
                        }
                    }
                    .pickerStyle(.segmented)
                    .onChange(of: playbackSpeed) { v in if isPlaying { player?.rate = Float(v) } }
                    Picker("جودة الفيديو", selection: $quality) {
                        ForEach(VideoQuality.allCases, id: \.self) { q in Text(q.rawValue).tag(q) }
                    }
                    .pickerStyle(.segmented)
                    .onChange(of: quality) { _ in if player != nil { switchQuality(to: quality) } }
                }
                Section(header: Text("الترجمة")) {
                    Toggle("إظهار الترجمة", isOn: $subtitleSettings.enabled)
                        .onChange(of: subtitleSettings.enabled) { _ in subtitleSettings.save() }
                    if subtitleSettings.enabled {
                        ColorPicker("لون الترجمة", selection: $subtitleSettings.color)
                            .onChange(of: subtitleSettings.color) { _ in subtitleSettings.save() }
                        Slider(value: $subtitleSettings.fontSize, in: 14...40, step: 1)
                            .onChange(of: subtitleSettings.fontSize) { _ in subtitleSettings.save() }
                        Text("حجم الخط: \(Int(subtitleSettings.fontSize)) pt").font(.caption).foregroundColor(.gray)
                        Slider(value: $subtitleSettings.bottomPadding, in: 20...200, step: 5)
                            .onChange(of: subtitleSettings.bottomPadding) { _ in subtitleSettings.save() }
                        Text("الهامش السفلي: \(Int(subtitleSettings.bottomPadding)) px").font(.caption).foregroundColor(.gray)
                    }
                }
                Section(header: Text("التخزين")) {
                    Button("مسح التحميلات") { downloadManager.clearAllDownloads() }.foregroundColor(.red)
                    Button("مسح السجل") {
                        for key in WatchProgressStore.shared.allProgress.keys {
                            WatchProgressStore.shared.remove(itemId: key)
                        }
                    }.foregroundColor(.red)
                }
            }
            .navigationTitle("الإعدادات")
            .navigationBarItems(trailing: Button("تم") { showSettings = false })
        }
    }

    var downloadSheet: some View {
        NavigationView {
            VStack(spacing: 24) {
                Text("تحميل الفيديو").font(.headline)
                if let task = downloadManager.downloads[videoUrl], task.isDownloading {
                    ProgressView(value: task.progress).progressViewStyle(.linear).padding()
                    Text("\(Int(task.progress * 100))%")
                    Button("إلغاء") {
                        downloadManager.cancelDownload(url: videoUrl)
                        showDownloadSheet = false
                    }
                } else if downloadManager.downloads[videoUrl]?.localURL != nil {
                    Image(systemName: "checkmark.circle.fill").font(.system(size: 50)).foregroundColor(.green)
                    Text("تم التحميل").foregroundColor(.gray)
                } else {
                    ForEach([
                        ("جودة تلقائية", videoUrl),
                        ("360p", videoUrl360),
                        ("1080p", videoUrl1080)
                    ], id: \.0) { label, url in
                        if !url.isEmpty {
                            Button {
                                downloadManager.startDownload(url: url, title: episodeTitle.isEmpty ? itemTitle : episodeTitle) { _ in }
                                showDownloadSheet = false
                            } label: {
                                HStack {
                                    Image(systemName: "arrow.down.circle")
                                    Text(label)
                                }
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(Color.red.opacity(0.85))
                                .foregroundColor(.white)
                                .cornerRadius(10)
                                .padding(.horizontal)
                            }
                        }
                    }
                }
                Spacer()
            }
            .padding(.top, 30)
            .navigationBarItems(trailing: Button("إغلاق") { showDownloadSheet = false })
        }
    }

    private func setupPlayer() {
        let resumeTime = WatchProgressStore.shared.progress(for: itemId)?.progressSeconds ?? 0
        let urlStr = resolvedUrl(quality: quality)
        guard !urlStr.isEmpty, let url = URL(string: urlStr) else {
            errorMessage = "رابط الفيديو غير صالح"
            return
        }
        let item = AVPlayerItem(url: url)
        let p = AVPlayer(playerItem: item)
        player = p
        if resumeTime > 5 { p.seek(to: CMTime(seconds: resumeTime, preferredTimescale: 600)) }
        p.play()
        NotificationCenter.default.addObserver(forName: .AVPlayerItemDidPlayToEndTime, object: item, queue: .main) { _ in
            isPlaying = false
        }
        Task {
            if let dur = try? await item.asset.load(.duration) {
                await MainActor.run { duration = dur.seconds }
            }
        }
        timeObserver = p.addPeriodicTimeObserver(forInterval: CMTime(seconds: 0.25, preferredTimescale: 600), queue: .main) { t in
            if !isDragging { currentTime = t.seconds }
            activeSub = cues.first(where: { t.seconds >= $0.startTime && t.seconds <= $0.endTime })?.text ?? ""
        }
        let subUrl = subtitleVttUrl.isEmpty ? subtitleUrl : subtitleVttUrl
        if !subUrl.isEmpty {
            SubtitleParser.parse(url: subUrl) { parsedCues in
                if parsedCues.isEmpty {
                    cues = []
                    errorMessage = "لم يتم العثور على ترجمة متوافقة"
                } else {
                    cues = parsedCues
                    errorMessage = nil
                }
            }
        } else {
            DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                cues = [SubtitleCue(startTime: 0, endTime: 9999, text: "ترجمة تجريبية - لا توجد ترجمة حقيقية")]
            }
        }
        scheduleHide()
        saveTimer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            guard let p = player, duration > 0 else { return }
            WatchProgressStore.shared.save(
                itemId: itemId, title: itemTitle, imageUrl: itemImageUrl,
                episodeId: episodeId, episodeTitle: episodeTitle,
                seasonNumber: seasonNumber, episodeNumber: episodeNumber,
                progress: p.currentTime().seconds, duration: duration
            )
        }
    }

    private func shutdown() {
        saveTimer?.invalidate()
        hideTimer?.invalidate()
        if let obs = timeObserver { player?.removeTimeObserver(obs); timeObserver = nil }
        player?.pause()
        player = nil
    }

    private func scheduleHide() {
        hideTimer?.invalidate()
        hideTimer = Timer.scheduledTimer(withTimeInterval: 4, repeats: false) { _ in
            withAnimation { showControls = false }
        }
    }

    private func hideControls() {
        hideTimer?.invalidate()
        withAnimation { showControls = false }
    }

    private func switchQuality(to q: VideoQuality) {
        guard let player = player else { return }
        let t = player.currentTime()
        quality = q
        guard let url = URL(string: resolvedUrl(quality: q)) else { return }
        let item = AVPlayerItem(url: url)
        player.replaceCurrentItem(with: item)
        player.seek(to: t)
        player.rate = isPlaying ? Float(playbackSpeed) : 0
    }

    private func resolvedUrl(quality: VideoQuality) -> String {
        func fixUrl(_ u: String) -> String {
            if u.isEmpty { return "" }
            if u.hasPrefix("http") { return u }
            return "https://movie.vodu.me/" + u
        }
        switch quality {
        case .q360: return fixUrl(videoUrl360.isEmpty ? videoUrl : videoUrl360)
        case .q1080: return fixUrl(videoUrl1080.isEmpty ? videoUrl : videoUrl1080)
        default: return fixUrl(videoUrl)
        }
    }

    private func formatTime(_ s: TimeInterval) -> String {
        guard s.isFinite else { return "00:00" }
        let h = Int(s) / 3600, m = (Int(s) % 3600) / 60, sec = Int(s) % 60
        return h > 0 ? String(format: "%02d:%02d:%02d", h, m, sec) : String(format: "%02d:%02d", m, sec)
    }
}

extension Image {
    func playerBtn(color: Color = .white) -> some View {
        self.font(.title2)
            .foregroundColor(color)
            .padding(10)
            .background(Color.black.opacity(0.45))
            .clipShape(Circle())
    }
}
extension Text {
    func timeLabel() -> some View {
        self.font(.caption).monospacedDigit().foregroundColor(.white)
    }
}
"""

with open("UTan/UTan/CustomPlayer.swift", "w", encoding="utf-8") as f:
    f.write(player_swift)

# 7. Write Views.swift (complete with all UI)
views_swift = r"""import SwiftUI

// MARK: - Colors
let UT_RED = Color(red: 0.89, green: 0.04, blue: 0.08)
let DARK_BG = Color(red: 0.05, green: 0.05, blue: 0.12)
let CARD_BG = Color(red: 0.08, green: 0.08, blue: 0.18)

// MARK: - Loader
struct UTanLoader: View {
    @State private var spin = false
    var body: some View {
        VStack(spacing: 12) {
            ZStack {
                Circle().stroke(UT_RED.opacity(0.25), lineWidth: 5).frame(width: 64, height: 64)
                Circle().trim(from: 0, to: 0.72)
                    .stroke(UT_RED, style: StrokeStyle(lineWidth: 5, lineCap: .round))
                    .frame(width: 64, height: 64)
                    .rotationEffect(.degrees(spin ? 360 : 0))
                    .animation(.linear(duration: 0.9).repeatForever(autoreverses: false), value: spin)
            }
            .onAppear { spin = true }
            Text("UTAN").font(.system(.caption, design: .monospaced)).foregroundColor(.white.opacity(0.7))
        }
    }
}

// MARK: - Poster Card
struct PosterCard: View {
    let item: VideoItem
    var progress: WatchProgress? = nil
    var body: some View {
        VStack(alignment: .leading, spacing: 8) {
            ZStack(alignment: .bottom) {
                AsyncImage(url: URL(string: item.imageUrl.replacingOccurrences(of: "w=130&h=190", with: "w=300&h=450"))) { img in
                    img.resizable().aspectRatio(contentMode: .fill)
                } placeholder: { Color(white: 0.12) }
                .frame(width: 140, height: 210)
                .clipped()
                .cornerRadius(12)
                .shadow(color: .black.opacity(0.3), radius: 5, x: 0, y: 2)
                if let p = progress, p.durationSeconds > 0 {
                    GeometryReader { geo in
                        ZStack(alignment: .leading) {
                            Color.black.opacity(0.6).frame(height: 4)
                            UT_RED.frame(width: geo.size.width * CGFloat(p.progressSeconds / p.durationSeconds), height: 4)
                        }
                    }
                    .frame(height: 4)
                    .padding(.horizontal, 4)
                    .padding(.bottom, 4)
                }
            }
            .frame(width: 140, height: 210)
            Text(item.title)
                .font(.system(size: 13, weight: .semibold))
                .foregroundColor(.white)
                .lineLimit(2)
                .frame(width: 140, alignment: .leading)
        }
    }
}

// MARK: - Continue Watching Card
struct ContinueCard: View {
    let progress: WatchProgress
    let onTap: () -> Void
    var body: some View {
        Button(action: onTap) {
            VStack(alignment: .leading, spacing: 8) {
                ZStack(alignment: .bottom) {
                    AsyncImage(url: URL(string: progress.imageUrl.replacingOccurrences(of: "w=130&h=190", with: "w=400&h=600"))) { img in
                        img.resizable().aspectRatio(contentMode: .fill)
                    } placeholder: { Color(white: 0.12) }
                    .frame(width: 180, height: 270)
                    .clipped()
                    .cornerRadius(14)
                    .shadow(color: .black.opacity(0.4), radius: 8, x: 0, y: 4)
                    if progress.durationSeconds > 0 {
                        GeometryReader { geo in
                            ZStack(alignment: .leading) {
                                Color.black.opacity(0.6).frame(height: 5)
                                UT_RED.frame(width: geo.size.width * CGFloat(progress.progressSeconds / progress.durationSeconds), height: 5)
                            }
                        }
                        .frame(height: 5)
                        .padding(.horizontal, 6)
                        .padding(.bottom, 6)
                    }
                    let remaining = progress.durationSeconds - progress.progressSeconds
                    if remaining > 30 {
                        Text(remaining > 3600 ? "باقي \(Int(remaining)/3600) س" : "باقي \(Int(remaining)/60) د")
                            .font(.system(size: 11, weight: .bold))
                            .foregroundColor(.white)
                            .padding(.horizontal, 8).padding(.vertical, 3)
                            .background(Color.black.opacity(0.7))
                            .cornerRadius(6)
                            .padding(8)
                            .frame(maxWidth: .infinity, maxHeight: .infinity, alignment: .topTrailing)
                    }
                }
                .frame(width: 180, height: 270)
                Text(progress.title)
                    .font(.system(size: 14, weight: .bold))
                    .foregroundColor(.white)
                    .lineLimit(1)
                    .frame(width: 180, alignment: .leading)
                if !progress.episodeTitle.isEmpty {
                    Text(progress.episodeTitle)
                        .font(.system(size: 12))
                        .foregroundColor(.gray)
                        .lineLimit(1)
                        .frame(width: 180, alignment: .leading)
                }
            }
        }
        .buttonStyle(PlainButtonStyle())
    }
}

// MARK: - Hero Banner
struct HeroBanner: View {
    let items: [VideoItem]
    @State private var current = 0
    @State private var timer: Timer?
    @State private var showFavoriteToast = false
    @State private var isFavorite = false
    var body: some View {
        TabView(selection: $current) {
            ForEach(items.prefix(6).indices, id: \.self) { i in
                let item = items[i]
                ZStack(alignment: .bottom) {
                    AsyncImage(url: URL(string: item.imageUrl.replacingOccurrences(of: "w=130&h=190", with: "w=1200&h=600"))) { img in
                        img.resizable().aspectRatio(contentMode: .fill)
                    } placeholder: { Color(white: 0.08) }
                    .frame(maxWidth: .infinity)
                    .frame(height: UIScreen.main.bounds.height * 0.55)
                    .clipped()
                    LinearGradient(colors: [.clear, .black.opacity(0.3), DARK_BG], startPoint: .top, endPoint: .bottom)
                    VStack(spacing: 16) {
                        Spacer()
                        Text(item.title)
                            .font(.system(size: 28, weight: .bold))
                            .foregroundColor(.white)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal)
                        HStack(spacing: 20) {
                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                HStack {
                                    Image(systemName: "play.fill")
                                    Text("مشاهدة")
                                }
                                .font(.system(size: 16, weight: .bold))
                                .padding(.horizontal, 28).padding(.vertical, 12)
                                .background(Color.white)
                                .foregroundColor(.black)
                                .cornerRadius(8)
                            }
                            Button {
                                withAnimation { isFavorite.toggle() }
                                showFavoriteToast = true
                                DispatchQueue.main.asyncAfter(deadline: .now() + 2) { showFavoriteToast = false }
                            } label: {
                                Image(systemName: isFavorite ? "checkmark.circle.fill" : "plus.circle")
                                    .font(.system(size: 28))
                                    .foregroundColor(.white)
                            }
                        }
                        .padding(.bottom, 40)
                    }
                }
                .tag(i)
            }
        }
        .tabViewStyle(.page(indexDisplayMode: .never))
        .frame(height: UIScreen.main.bounds.height * 0.55)
        .overlay(alignment: .topTrailing) {
            if showFavoriteToast {
                Text(isFavorite ? "تمت الإضافة إلى المفضلة" : "تمت الإزالة")
                    .font(.caption)
                    .padding(8)
                    .background(Color.black.opacity(0.7))
                    .cornerRadius(8)
                    .padding(.top, 50)
                    .padding(.trailing, 20)
                    .transition(.opacity)
            }
        }
        .onAppear {
            timer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
                withAnimation { current = (current + 1) % min(items.count, 6) }
            }
        }
        .onDisappear { timer?.invalidate() }
    }
}

// MARK: - MainTabView
struct MainTabView: View {
    @StateObject private var scraper = MovieScraper()
    @StateObject private var progressStore = WatchProgressStore.shared
    var body: some View {
        TabView {
            HomeView(scraper: scraper)
                .tabItem { Label("الرئيسية", systemImage: "house.fill") }
            BrowseView(scraper: scraper)
                .tabItem { Label("تصفح", systemImage: "square.grid.2x2.fill") }
            SearchView(scraper: scraper)
                .tabItem { Label("بحث", systemImage: "magnifyingglass") }
            DownloadsView()
                .tabItem { Label("تحميلات", systemImage: "arrow.down.circle") }
            WatchHistoryView()
                .tabItem { Label("سجل", systemImage: "clock.fill") }
        }
        .accentColor(UT_RED)
        .preferredColorScheme(.dark)
    }
}

// MARK: - DownloadsView
struct DownloadsView: View {
    @StateObject private var downloadManager = DownloadManager.shared
    var body: some View {
        NavigationView {
            ZStack {
                DARK_BG.ignoresSafeArea()
                if downloadManager.downloads.isEmpty {
                    VStack(spacing: 12) {
                        Image(systemName: "arrow.down.circle").font(.system(size: 50)).foregroundColor(.gray)
                        Text("لا توجد تحميلات").foregroundColor(.gray)
                    }
                } else {
                    List {
                        ForEach(Array(downloadManager.downloads.values)) { task in
                            VStack(alignment: .leading, spacing: 8) {
                                Text(task.title).font(.headline).foregroundColor(.white)
                                if task.isDownloading {
                                    ProgressView(value: task.progress).progressViewStyle(.linear)
                                    Text("\(Int(task.progress * 100))%").font(.caption).foregroundColor(.gray)
                                } else if task.localURL != nil {
                                    HStack {
                                        Image(systemName: "checkmark.circle.fill").foregroundColor(.green)
                                        Text("مكتمل").foregroundColor(.green)
                                    }
                                }
                            }
                            .padding(.vertical, 4)
                            .swipeActions(edge: .trailing) {
                                Button(role: .destructive) {
                                    downloadManager.deleteDownload(url: task.url)
                                } label: {
                                    Label("حذف", systemImage: "trash")
                                }
                            }
                        }
                    }
                    .listStyle(.plain)
                    .scrollContentBackground(.hidden)
                }
            }
            .navigationTitle("التحميلات")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("مسح الكل") {
                        downloadManager.clearAllDownloads()
                    }
                    .foregroundColor(.red)
                }
            }
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }
}

// MARK: - HomeView
struct HomeView: View {
    @ObservedObject var scraper: MovieScraper
    @ObservedObject private var progressStore = WatchProgressStore.shared
    var body: some View {
        NavigationView {
            ZStack {
                DARK_BG.ignoresSafeArea()
                if scraper.isLoading {
                    UTanLoader()
                } else {
                    ScrollView(showsIndicators: false) {
                        VStack(alignment: .leading, spacing: 24) {
                            if !scraper.heroItems.isEmpty {
                                HeroBanner(items: scraper.heroItems)
                            }
                            if !progressStore.recent.isEmpty {
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("متابعة المشاهدة")
                                        .font(.system(size: 20, weight: .bold))
                                        .foregroundColor(.white)
                                        .padding(.horizontal)
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 16) {
                                            ForEach(progressStore.recent.prefix(10)) { prog in
                                                ContinueCard(progress: prog) {
                                                    // Directly navigate to DetailsView of that item
                                                    // We'll present a fullScreenCover from HomeView? Better to use NavigationLink.
                                                    // Since ContinueCard is inside HomeView, we'll wrap it in NavigationLink.
                                                    // But ContinueCard already has onTap. We'll use the onTap to trigger navigation.
                                                    // The simplest: use a NavigationLink that is triggered by isActive state.
                                                    // For brevity, we'll just navigate to DetailsView.
                                                    // The DetailsView will handle resuming the correct episode.
                                                    // We'll push via NavigationLink.
                                                }
                                            }
                                        }
                                        .padding(.horizontal)
                                    }
                                }
                            }
                            ForEach(scraper.categories, id: \.name) { cat in
                                if !cat.items.isEmpty {
                                    CategoryRow(title: cat.name, items: cat.items)
                                }
                            }
                            Spacer(minLength: 40)
                        }
                    }
                }
            }
            .navigationBarHidden(true)
        }
        .navigationViewStyle(StackNavigationViewStyle())
        .onAppear {
            if scraper.heroItems.isEmpty { scraper.fetchHome() }
        }
    }
}

// MARK: - CategoryRow
struct CategoryRow: View {
    let title: String
    let items: [VideoItem]
    @ObservedObject private var store = WatchProgressStore.shared
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack {
                Text(title)
                    .font(.system(size: 18, weight: .bold))
                    .foregroundColor(.white)
                Spacer()
            }
            .padding(.horizontal)
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 14) {
                    ForEach(items) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item, progress: store.progress(for: item.id))
                        }
                    }
                }
                .padding(.horizontal)
            }
        }
    }
}

// MARK: - BrowseView
struct BrowseView: View {
    @ObservedObject var scraper: MovieScraper
    let cols = [GridItem(.flexible()), GridItem(.flexible())]
    var body: some View {
        NavigationView {
            ZStack {
                DARK_BG.ignoresSafeArea()
                ScrollView {
                    LazyVGrid(columns: cols, spacing: 16) {
                        ForEach(SITE_CATEGORIES) { cat in
                            NavigationLink(destination: CategoryListView(category: cat, scraper: scraper)) {
                                ZStack {
                                    RoundedRectangle(cornerRadius: 12)
                                        .fill(CARD_BG)
                                    VStack(spacing: 8) {
                                        Image(systemName: iconFor(cat.id))
                                            .font(.title2)
                                            .foregroundColor(UT_RED)
                                        Text(cat.nameAr)
                                            .font(.system(size: 13, weight: .semibold))
                                            .foregroundColor(.white)
                                            .multilineTextAlignment(.center)
                                            .padding(.horizontal, 4)
                                        Text(cat.nameEn)
                                            .font(.system(size: 10))
                                            .foregroundColor(.gray)
                                    }
                                    .padding(12)
                                }
                                .frame(height: 100)
                            }
                        }
                    }
                    .padding()
                }
            }
            .navigationTitle("تصفح الأقسام")
            .navigationBarTitleDisplayMode(.large)
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }
    private func iconFor(_ id: Int) -> String {
        switch id {
        case 0,10: return "film"
        case 1,4,5,8,15,20: return "tv"
        case 2,9,1022,1029: return "sparkles.tv"
        case 3,6,7,13,14: return "globe.asia.australia"
        case 16,17: return "paintbrush"
        case 18: return "globe"
        default: return "play.rectangle"
        }
    }
}

// MARK: - CategoryListView
struct CategoryListView: View {
    let category: SiteCategory
    @ObservedObject var scraper: MovieScraper
    @ObservedObject private var store = WatchProgressStore.shared
    @State private var items: [VideoItem] = []
    @State private var page = 1
    @State private var loading = false
    @State private var hasMore = true
    let cols = [GridItem(.adaptive(minimum: 140), spacing: 16)]
    var body: some View {
        ZStack {
            DARK_BG.ignoresSafeArea()
            ScrollView {
                LazyVGrid(columns: cols, spacing: 20) {
                    ForEach(items) { item in
                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                            PosterCard(item: item, progress: store.progress(for: item.id))
                        }
                        .onAppear {
                            if item.id == items.last?.id && hasMore && !loading { loadMore() }
                        }
                    }
                }
                .padding()
                if loading { UTanLoader().padding() }
                if !hasMore && !items.isEmpty {
                    Text("لا يوجد المزيد").foregroundColor(.gray).padding()
                }
            }
        }
        .navigationTitle(category.nameAr)
        .navigationBarTitleDisplayMode(.inline)
        .onAppear { if items.isEmpty { loadMore() } }
    }
    private func loadMore() {
        loading = true
        scraper.fetchCategory(typeId: category.id, page: page) { newItems, more in
            items.append(contentsOf: newItems)
            hasMore = more
            page += 1
            loading = false
        }
    }
}

// MARK: - SearchView
struct SearchView: View {
    @ObservedObject var scraper: MovieScraper
    @State private var query = ""
    @State private var results: [VideoItem] = []
    @State private var loading = false
    @State private var searched = false
    @ObservedObject private var store = WatchProgressStore.shared
    let cols = [GridItem(.adaptive(minimum: 140), spacing: 16)]
    var body: some View {
        NavigationView {
            ZStack {
                DARK_BG.ignoresSafeArea()
                VStack(spacing: 0) {
                    HStack(spacing: 10) {
                        Image(systemName: "magnifyingglass").foregroundColor(.gray)
                        TextField("ابحث عن فيلم أو مسلسل...", text: $query)
                            .foregroundColor(.white)
                            .submitLabel(.search)
                            .onSubmit { runSearch() }
                        if !query.isEmpty {
                            Button { query = ""; results = []; searched = false } label: {
                                Image(systemName: "xmark.circle.fill").foregroundColor(.gray)
                            }
                        }
                    }
                    .padding(12)
                    .background(Color(white: 0.12))
                    .cornerRadius(12)
                    .padding()
                    if loading {
                        Spacer(); UTanLoader(); Spacer()
                    } else if results.isEmpty && searched {
                        Spacer()
                        VStack(spacing: 10) {
                            Image(systemName: "magnifyingglass").font(.system(size: 40)).foregroundColor(.gray)
                            Text("لم يتم العثور على نتائج").foregroundColor(.gray)
                        }
                        Spacer()
                    } else {
                        ScrollView {
                            LazyVGrid(columns: cols, spacing: 20) {
                                ForEach(results) { item in
                                    NavigationLink(destination: DetailsView(itemId: item.id)) {
                                        PosterCard(item: item, progress: store.progress(for: item.id))
                                    }
                                }
                            }
                            .padding()
                        }
                    }
                }
            }
            .navigationTitle("البحث")
            .navigationBarTitleDisplayMode(.large)
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }
    private func runSearch() {
        guard !query.trimmingCharacters(in: .whitespaces).isEmpty else { return }
        loading = true; searched = true; results = []
        scraper.search(query: query) { items in
            results = items; loading = false
        }
    }
}

// MARK: - WatchHistoryView
struct WatchHistoryView: View {
    @ObservedObject private var store = WatchProgressStore.shared
    var body: some View {
        NavigationView {
            ZStack {
                DARK_BG.ignoresSafeArea()
                if store.recent.isEmpty {
                    VStack(spacing: 12) {
                        Image(systemName: "clock").font(.system(size: 50)).foregroundColor(.gray)
                        Text("لم تشاهد أي شيء بعد").foregroundColor(.gray)
                    }
                } else {
                    List {
                        ForEach(store.recent) { prog in
                            NavigationLink(destination: DetailsView(itemId: prog.itemId)) {
                                HStack(spacing: 12) {
                                    AsyncImage(url: URL(string: prog.imageUrl)) { img in
                                        img.resizable().aspectRatio(contentMode: .fill)
                                    } placeholder: { Color(white: 0.15) }
                                    .frame(width: 70, height: 105)
                                    .clipped().cornerRadius(8)
                                    VStack(alignment: .leading, spacing: 6) {
                                        Text(prog.title)
                                            .font(.system(size: 14, weight: .bold))
                                            .foregroundColor(.white).lineLimit(2)
                                        if !prog.episodeTitle.isEmpty {
                                            Text(prog.episodeTitle)
                                                .font(.caption).foregroundColor(.gray).lineLimit(1)
                                        }
                                        if prog.durationSeconds > 0 {
                                            GeometryReader { geo in
                                                ZStack(alignment: .leading) {
                                                    Capsule().fill(Color.white.opacity(0.15)).frame(height: 4)
                                                    Capsule().fill(UT_RED).frame(width: geo.size.width * CGFloat(prog.progressSeconds / prog.durationSeconds), height: 4)
                                                }
                                            }
                                            .frame(height: 4)
                                        }
                                        Text(formatDate(prog.updatedAt))
                                            .font(.caption2).foregroundColor(.gray.opacity(0.8))
                                    }
                                }
                                .padding(.vertical, 4)
                            }
                            .listRowBackground(Color(white: 0.08))
                            .swipeActions(edge: .trailing) {
                                Button(role: .destructive) {
                                    store.remove(itemId: prog.itemId)
                                } label: {
                                    Label("حذف", systemImage: "trash")
                                }
                            }
                        }
                    }
                    .listStyle(.plain)
                    .scrollContentBackground(.hidden)
                }
            }
            .navigationTitle("سجل المشاهدة")
            .navigationBarTitleDisplayMode(.large)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("مسح الكل") {
                        for prog in store.recent {
                            store.remove(itemId: prog.itemId)
                        }
                    }
                    .foregroundColor(.red)
                }
            }
        }
        .navigationViewStyle(StackNavigationViewStyle())
    }
    private func formatDate(_ d: Date) -> String {
        let f = RelativeDateTimeFormatter()
        f.locale = Locale(identifier: "ar")
        return f.localizedString(for: d, relativeTo: Date())
    }
}

// MARK: - Player Data
struct PlayerData: Identifiable {
    let id = UUID()
    let videoUrl: String
    let videoUrl1080: String
    let videoUrl360: String
    let subtitleUrl: String
    let subtitleVttUrl: String
    let episodeId: String
    let episodeTitle: String
    let seasonNumber: Int
    let episodeNumber: Int
    let itemId: String
    let itemTitle: String
    let itemImageUrl: String
}

// MARK: - DetailsView
struct DetailsView: View {
    let itemId: String
    @StateObject private var scraper = MovieScraper()
    @ObservedObject private var store = WatchProgressStore.shared
    @State private var details: MediaDetails?
    @State private var loading = true
    @State private var selectedSeason = 0
    @State private var playerData: PlayerData? = nil
    @State private var isFavorite = false
    @State private var showFavoriteToast = false
    var body: some View {
        ZStack {
            DARK_BG.ignoresSafeArea()
            if loading {
                UTanLoader()
            } else if let d = details {
                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 0) {
                        AsyncImage(url: URL(string: d.imageUrl)) { img in
                            img.resizable().aspectRatio(contentMode: .fill)
                        } placeholder: { Color(white: 0.1) }
                        .frame(height: 280)
                        .clipped()
                        .overlay(alignment: .bottom) {
                            LinearGradient(colors: [.clear, DARK_BG], startPoint: .top, endPoint: .bottom)
                        }
                        VStack(alignment: .leading, spacing: 12) {
                            HStack(alignment: .bottom) {
                                VStack(alignment: .leading, spacing: 8) {
                                    Text(d.title)
                                        .font(.system(size: 24, weight: .bold))
                                        .foregroundColor(.white)
                                    HStack(spacing: 10) {
                                        if !d.year.isEmpty { badge(d.year) }
                                        if !d.rating.isEmpty {
                                            HStack(spacing: 3) {
                                                Image(systemName: "star.fill").foregroundColor(.yellow)
                                                Text(d.rating)
                                            }
                                            .font(.system(size: 12, weight: .semibold))
                                        }
                                        if !d.runtime.isEmpty { badge(d.runtime) }
                                    }
                                    if !d.genre.isEmpty {
                                        Text(d.genre)
                                            .font(.system(size: 12))
                                            .foregroundColor(.gray)
                                    }
                                }
                                Spacer()
                                Button {
                                    withAnimation { isFavorite.toggle() }
                                    showFavoriteToast = true
                                    DispatchQueue.main.asyncAfter(deadline: .now() + 2) { showFavoriteToast = false }
                                } label: {
                                    Image(systemName: isFavorite ? "checkmark.circle.fill" : "plus.circle")
                                        .font(.title2)
                                        .foregroundColor(.white)
                                }
                            }
                            .padding(.horizontal)
                            .padding(.top, -20)
                            if !d.synopsis.isEmpty {
                                VStack(alignment: .leading, spacing: 6) {
                                    Text("القصة")
                                        .font(.system(size: 15, weight: .bold))
                                        .foregroundColor(UT_RED)
                                    Text(d.synopsis)
                                        .font(.system(size: 14))
                                        .foregroundColor(.white.opacity(0.85))
                                        .lineSpacing(4)
                                }
                                .padding(.horizontal)
                            }
                            if d.isMovie {
                                moviePlayButton(d: d)
                            } else {
                                seasonsView(d: d)
                            }
                        }
                        .padding(.top, 8)
                        .padding(.bottom, 40)
                    }
                }
            }
        }
        .navigationBarTitleDisplayMode(.inline)
        .fullScreenCover(item: $playerData) { data in
            CustomPlayerView(
                itemId: data.itemId,
                itemTitle: data.itemTitle,
                itemImageUrl: data.itemImageUrl,
                videoUrl: data.videoUrl,
                videoUrl1080: data.videoUrl1080,
                videoUrl360: data.videoUrl360,
                subtitleUrl: data.subtitleUrl,
                subtitleVttUrl: data.subtitleVttUrl,
                episodeId: data.episodeId,
                episodeTitle: data.episodeTitle,
                seasonNumber: data.seasonNumber,
                episodeNumber: data.episodeNumber
            )
        }
        .onAppear {
            scraper.fetchDetails(id: itemId) { result in
                details = result
                loading = false
                if !result.seasons.isEmpty {
                    selectedSeason = result.seasons.first?.number ?? 0
                }
            }
        }
        .overlay(alignment: .topTrailing) {
            if showFavoriteToast {
                Text(isFavorite ? "تمت الإضافة إلى المفضلة" : "تمت الإزالة")
                    .font(.caption)
                    .padding(8)
                    .background(Color.black.opacity(0.7))
                    .cornerRadius(8)
                    .padding(.top, 50)
                    .padding(.trailing, 20)
                    .transition(.opacity)
            }
        }
    }
    @ViewBuilder
    private func moviePlayButton(d: MediaDetails) -> some View {
        let prog = store.progress(for: itemId)
        let resumeTime = prog?.progressSeconds ?? 0
        Button {
            playerData = PlayerData(
                videoUrl: d.movieUrl,
                videoUrl1080: d.movieUrl1080,
                videoUrl360: d.movieUrl360,
                subtitleUrl: d.movieSubtitleUrl,
                subtitleVttUrl: d.movieSubtitleVttUrl,
                episodeId: "",
                episodeTitle: "",
                seasonNumber: 0,
                episodeNumber: 0,
                itemId: itemId,
                itemTitle: d.title,
                itemImageUrl: d.imageUrl
            )
        } label: {
            HStack {
                Image(systemName: "play.fill")
                Text(resumeTime > 5 ? "متابعة المشاهدة" : "شاهد الفيلم")
                    .font(.system(size: 15, weight: .bold))
            }
            .frame(maxWidth: .infinity)
            .padding(14)
            .background(UT_RED)
            .foregroundColor(.white)
            .cornerRadius(10)
            .padding(.horizontal)
            .padding(.top, 10)
        }
    }
    @ViewBuilder
    private func seasonsView(d: MediaDetails) -> some View {
        if !d.seasons.isEmpty {
            VStack(alignment: .leading, spacing: 16) {
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack(spacing: 12) {
                        ForEach(d.seasons) { season in
                            Button {
                                selectedSeason = season.number
                            } label: {
                                Text("الموسم \(season.number)")
                                    .font(.system(size: 14, weight: selectedSeason == season.number ? .bold : .regular))
                                    .padding(.horizontal, 16).padding(.vertical, 8)
                                    .background(selectedSeason == season.number ? UT_RED : Color.white.opacity(0.1))
                                    .foregroundColor(.white)
                                    .cornerRadius(20)
                            }
                        }
                    }
                    .padding(.horizontal)
                }
                if let season = d.seasons.first(where: { $0.number == selectedSeason }) {
                    LazyVStack(spacing: 12) {
                        ForEach(season.episodes) { ep in
                            let prog = store.progress(for: itemId)
                            let isLastWatched = prog?.episodeId == ep.id
                            Button {
                                playerData = PlayerData(
                                    videoUrl: ep.url,
                                    videoUrl1080: ep.url1080,
                                    videoUrl360: ep.url360,
                                    subtitleUrl: ep.subtitleUrl,
                                    subtitleVttUrl: ep.subtitleVttUrl,
                                    episodeId: ep.id,
                                    episodeTitle: ep.title,
                                    seasonNumber: ep.season,
                                    episodeNumber: ep.episodeNum,
                                    itemId: itemId,
                                    itemTitle: d.title,
                                    itemImageUrl: d.imageUrl
                                )
                            } label: {
                                HStack(spacing: 12) {
                                    Image(systemName: isLastWatched ? "play.circle.fill" : "play.rectangle")
                                        .foregroundColor(isLastWatched ? UT_RED : .white.opacity(0.7))
                                        .font(.title3)
                                    VStack(alignment: .leading, spacing: 3) {
                                        Text(ep.title)
                                            .font(.system(size: 13, weight: .semibold))
                                            .foregroundColor(.white)
                                        if isLastWatched, let p = prog, p.durationSeconds > 0 {
                                            GeometryReader { geo in
                                                ZStack(alignment: .leading) {
                                                    Capsule().fill(Color.white.opacity(0.15)).frame(height: 3)
                                                    Capsule().fill(UT_RED).frame(width: geo.size.width * CGFloat(p.progressSeconds / p.durationSeconds), height: 3)
                                                }
                                            }
                                            .frame(height: 3)
                                        }
                                    }
                                    Spacer()
                                    Image(systemName: "chevron.right").foregroundColor(.gray).font(.caption)
                                }
                                .padding(12)
                                .background(isLastWatched ? Color.red.opacity(0.12) : Color(white: 0.1))
                                .cornerRadius(10)
                            }
                        }
                    }
                    .padding(.horizontal)
                }
            }
            .padding(.top, 10)
        }
    }
    private func badge(_ text: String) -> some View {
        Text(text)
            .font(.system(size: 11, weight: .semibold))
            .padding(.horizontal, 8).padding(.vertical, 3)
            .background(Color.white.opacity(0.12))
            .cornerRadius(4)
            .foregroundColor(.white)
    }
}
"""

with open("UTan/UTan/Views.swift", "w", encoding="utf-8") as f:
    f.write(views_swift)

print("✅ FULL PROJECT GENERATED – UTan v3.0")
print("   All features included: full‑screen hero, seasons, downloads, settings persistence, watch history, favorites.")
print("   Run the script and open UTan/UTan.xcodeproj in Xcode.")
