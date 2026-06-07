import os

# Create directory structure
os.makedirs("UTan/UTan.xcodeproj", exist_ok=True)
os.makedirs("UTan/UTan", exist_ok=True)

# 1. Write project.pbxproj (محدث ليشمل إعدادات CoreData و Network)
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
		010101012C12345600000005 /* CustomPlayerView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000006 /* CustomPlayerView.swift */; };
		010101012C12345600000007 /* SubtitleParser.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000008 /* SubtitleParser.swift */; };
		010101012C12345600000009 /* Models.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000000A /* Models.swift */; };
		010101012C1234560000000B /* PersistenceController.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000000C /* PersistenceController.swift */; };
		010101012C1234560000000D /* DownloadManager.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000000E /* DownloadManager.swift */; };
		010101012C1234560000000F /* HomeView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000010 /* HomeView.swift */; };
		010101012C12345600000011 /* SearchView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000012 /* SearchView.swift */; };
		010101012C12345600000013 /* CategoryListView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000014 /* CategoryListView.swift */; };
		010101012C12345600000015 /* DetailsView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000016 /* DetailsView.swift */; };
		010101012C12345600000017 /* DownloadsView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C12345600000018 /* DownloadsView.swift */; };
		010101012C12345600000019 /* ProfileView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000001A /* ProfileView.swift */; };
		010101012C1234560000001B /* MainTabView.swift in Sources */ = {isa = PBXBuildFile; fileRef = 010101012C1234560000001C /* MainTabView.swift */; };
/* End PBXBuildFile section */

/* Begin PBXFileReference section */
		010101012C12345600000002 /* UTanApp.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = UTanApp.swift; sourceTree = "<group>"; };
		010101012C12345600000004 /* Scraper.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Scraper.swift; sourceTree = "<group>"; };
		010101012C12345600000006 /* CustomPlayerView.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = CustomPlayerView.swift; sourceTree = "<group>"; };
		010101012C12345600000008 /* SubtitleParser.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = SubtitleParser.swift; sourceTree = "<group>"; };
		010101012C1234560000000A /* Models.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = Models.swift; sourceTree = "<group>"; };
		010101012C1234560000000C /* PersistenceController.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = PersistenceController.swift; sourceTree = "<group>"; };
		010101012C1234560000000E /* DownloadManager.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = DownloadManager.swift; sourceTree = "<group>"; };
		010101012C12345600000010 /* HomeView.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = HomeView.swift; sourceTree = "<group>"; };
		010101012C12345600000012 /* SearchView.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = SearchView.swift; sourceTree = "<group>"; };
		010101012C12345600000014 /* CategoryListView.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = CategoryListView.swift; sourceTree = "<group>"; };
		010101012C12345600000016 /* DetailsView.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = DetailsView.swift; sourceTree = "<group>"; };
		010101012C12345600000018 /* DownloadsView.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = DownloadsView.swift; sourceTree = "<group>"; };
		010101012C1234560000001A /* ProfileView.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = ProfileView.swift; sourceTree = "<group>"; };
		010101012C1234560000001C /* MainTabView.swift */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = sourcecode.swift; path = MainTabView.swift; sourceTree = "<group>"; };
		010101012C1234560000001D /* Info.plist */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.plist.xml; path = Info.plist; sourceTree = "<group>"; };
		010101012C1234560000001E /* UTan.app */ = {isa = PBXFileReference; explicitFileType = wrapper.application; includeInIndex = 0; path = UTan.app; sourceTree = BUILT_PRODUCTS_DIR; };
/* End PBXFileReference section */

/* Begin PBXFrameworksBuildPhase section */
		010101012C1234560000001F /* Frameworks */ = {
			isa = PBXFrameworksBuildPhase;
			buildActionMask = 2147483647;
			files = (
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXFrameworksBuildPhase section */

/* Begin PBXGroup section */
		010101012C12345600000020 /* MainGroup */ = {
			isa = PBXGroup;
			children = (
				010101012C12345600000021 /* UTan */,
				010101012C1234560000001E /* UTan.app */,
			);
			sourceTree = "<group>";
		};
		010101012C12345600000021 /* UTan */ = {
			isa = PBXGroup;
			children = (
				010101012C12345600000002 /* UTanApp.swift */,
				010101012C12345600000004 /* Scraper.swift */,
				010101012C12345600000006 /* CustomPlayerView.swift */,
				010101012C12345600000008 /* SubtitleParser.swift */,
				010101012C1234560000000A /* Models.swift */,
				010101012C1234560000000C /* PersistenceController.swift */,
				010101012C1234560000000E /* DownloadManager.swift */,
				010101012C12345600000010 /* HomeView.swift */,
				010101012C12345600000012 /* SearchView.swift */,
				010101012C12345600000014 /* CategoryListView.swift */,
				010101012C12345600000016 /* DetailsView.swift */,
				010101012C12345600000018 /* DownloadsView.swift */,
				010101012C1234560000001A /* ProfileView.swift */,
				010101012C1234560000001C /* MainTabView.swift */,
				010101012C1234560000001D /* Info.plist */,
			);
			path = UTan;
			sourceTree = "<group>";
		};
/* End PBXGroup section */

/* Begin PBXNativeTarget section */
		010101012C12345600000022 /* UTan */ = {
			isa = PBXNativeTarget;
			buildConfigurationList = 010101012C12345600000023 /* Build configuration list for PBXNativeTarget "UTan" */;
			buildPhases = (
				010101012C12345600000024 /* Sources */,
				010101012C1234560000001F /* Frameworks */,
			);
			buildRules = (
			);
			dependencies = (
			);
			name = UTan;
			productName = UTan;
			productReference = 010101012C1234560000001E /* UTan.app */;
			productType = "com.apple.product-type.application";
		};
/* End PBXNativeTarget section */

/* Begin PBXProject section */
		010101012C12345600000025 /* Project object */ = {
			isa = PBXProject;
			attributes = {
				LastSwiftUpdateCheck = 1500;
				LastUpgradeCheck = 1500;
				TargetAttributes = {
					010101012C12345600000022 = {
						CreatedOnToolsVersion = 15.0;
						DevelopmentTeam = "";
					};
				};
			};
			buildConfigurationList = 010101012C12345600000026 /* Build configuration list for PBXProject "UTan" */;
			compatibilityVersion = "Xcode 14.0";
			developmentRegion = en;
			hasScannedForEncodings = 0;
			knownRegions = (
				en,
				Base,
			);
			mainGroup = 010101012C12345600000020 /* MainGroup */;
			productRefGroup = 010101012C12345600000020 /* MainGroup */;
			projectDirPath = "";
			projectRoot = "";
			targets = (
				010101012C12345600000022 /* UTan */,
			);
		};
/* End PBXProject section */

/* Begin PBXSourcesBuildPhase section */
		010101012C12345600000024 /* Sources */ = {
			isa = PBXSourcesBuildPhase;
			buildActionMask = 2147483647;
			files = (
				010101012C12345600000001 /* UTanApp.swift in Sources */,
				010101012C12345600000003 /* Scraper.swift in Sources */,
				010101012C12345600000005 /* CustomPlayerView.swift in Sources */,
				010101012C12345600000007 /* SubtitleParser.swift in Sources */,
				010101012C12345600000009 /* Models.swift in Sources */,
				010101012C1234560000000B /* PersistenceController.swift in Sources */,
				010101012C1234560000000D /* DownloadManager.swift in Sources */,
				010101012C1234560000000F /* HomeView.swift in Sources */,
				010101012C12345600000011 /* SearchView.swift in Sources */,
				010101012C12345600000013 /* CategoryListView.swift in Sources */,
				010101012C12345600000015 /* DetailsView.swift in Sources */,
				010101012C12345600000017 /* DownloadsView.swift in Sources */,
				010101012C12345600000019 /* ProfileView.swift in Sources */,
				010101012C1234560000001B /* MainTabView.swift in Sources */,
			);
			runOnlyForDeploymentPostprocessing = 0;
		};
/* End PBXSourcesBuildPhase section */

/* Begin XCBuildConfiguration section */
		010101012C12345600000027 /* Debug */ = {
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
		010101012C12345600000028 /* Release */ = {
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
		010101012C12345600000029 /* Debug */ = {
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
		010101012C1234560000002A /* Release */ = {
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
		010101012C12345600000023 /* Build configuration list for PBXNativeTarget "UTan" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				010101012C12345600000029 /* Debug */,
				010101012C1234560000002A /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
		010101012C12345600000026 /* Build configuration list for PBXProject "UTan" */ = {
			isa = XCConfigurationList;
			buildConfigurations = (
				010101012C12345600000027 /* Debug */,
				010101012C12345600000028 /* Release */,
			);
			defaultConfigurationIsVisible = 0;
			defaultConfigurationName = Release;
		};
/* End XCConfigurationList section */
	};
	rootObject = 010101012C12345600000025 /* Project object */;
}
"""

with open("UTan/UTan.xcodeproj/project.pbxproj", "w", encoding="utf-8") as f:
    f.write(pbxproj_content)

# 2. Write Info.plist (مع إضافة أذونات التحميل)
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
    let persistenceController = PersistenceController.shared
    
    var body: some Scene {
        WindowGroup {
            MainTabView()
                .environment(\.managedObjectContext, persistenceController.container.viewContext)
        }
    }
}
"""

with open("UTan/UTan/UTanApp.swift", "w", encoding="utf-8") as f:
    f.write(app_swift)

# 4. Write Models.swift
models_swift = """import Foundation

struct VideoItem: Identifiable, Hashable {
    let id: String
    let title: String
    let imageUrl: String
    let type: String  // "post" for movies/series
}

struct EpisodeItem: Identifiable, Hashable {
    let id: String
    let title: String
    let url: String
    let url360: String
    let url1080: String
    let url4k: String
    let subtitleUrl: String
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
    var movieUrl360: String = ""
    var movieUrl1080: String = ""
    var movieUrl4k: String = ""
    var movieSubtitleUrl: String = ""
    var episodes: [EpisodeItem] = []
    var similarItems: [VideoItem] = []
}

enum VideoQuality: String, CaseIterable {
    case p360 = "360p"
    case p720 = "720p"
    case p1080 = "1080p"
    case p4K = "4K"
}

struct DownloadTask: Identifiable {
    let id = UUID()
    let videoId: String  // episode id or movie id
    let title: String
    let imageUrl: String
    let quality: VideoQuality
    let localURL: URL?
    var progress: Double = 0.0
    var isDownloading = false
}
"""

with open("UTan/UTan/Models.swift", "w", encoding="utf-8") as f:
    f.write(models_swift)

# 5. Write PersistenceController.swift (CoreData)
persistence_swift = """import CoreData

struct PersistenceController {
    static let shared = PersistenceController()
    
    let container: NSPersistentContainer
    
    init() {
        container = NSPersistentContainer(name: "UTanDataModel")
        container.loadPersistentStores { _, error in
            if let error = error as NSError? {
                fatalError("Unresolved error \\(error), \\(error.userInfo)")
            }
        }
        container.viewContext.automaticallyMergesChangesFromParent = true
    }
    
    func saveContext() {
        let context = container.viewContext
        if context.hasChanges {
            do {
                try context.save()
            } catch {
                let nsError = error as NSError
                fatalError("Unresolved error \\(nsError), \\(nsError.userInfo)")
            }
        }
    }
}
"""

with open("UTan/UTan/PersistenceController.swift", "w", encoding="utf-8") as f:
    f.write(persistence_swift)

# 6. Write DownloadManager.swift
download_manager_swift = """import Foundation
import SwiftUI
import Combine

class DownloadManager: NSObject, ObservableObject, URLSessionDownloadDelegate {
    static let shared = DownloadManager()
    
    @Published var downloads: [String: DownloadTask] = [:] // videoId -> task
    
    private var session: URLSession!
    private var activeDownloads: [URL: DownloadTask] = [:]
    
    override init() {
        super.init()
        let config = URLSessionConfiguration.background(withIdentifier: "com.mustaqil.utan.downloads")
        session = URLSession(configuration: config, delegate: self, delegateQueue: OperationQueue.main)
        // Restore previous downloads
        session.getAllTasks { tasks in
            for task in tasks {
                if let originalRequest = task.originalRequest,
                   let url = originalRequest.url {
                    let downloadTask = DownloadTask(videoId: url.absoluteString, title: "", imageUrl: "", quality: .p720, localURL: nil, progress: 0.0, isDownloading: true)
                    self.activeDownloads[url] = downloadTask
                    self.downloads[url.absoluteString] = downloadTask
                }
            }
        }
    }
    
    func startDownload(videoId: String, title: String, imageUrl: String, quality: VideoQuality, videoURL: URL) {
        let task = session.downloadTask(with: videoURL)
        let downloadTask = DownloadTask(videoId: videoId, title: title, imageUrl: imageUrl, quality: quality, localURL: nil, progress: 0.0, isDownloading: true)
        downloads[videoId] = downloadTask
        activeDownloads[videoURL] = downloadTask
        task.resume()
    }
    
    func cancelDownload(videoId: String, videoURL: URL) {
        if let task = activeDownloads.first(where: { $0.key == videoURL }) {
            session.invalidateAndCancel()
            downloads.removeValue(forKey: videoId)
            activeDownloads.removeValue(forKey: videoURL)
        }
    }
    
    func isDownloaded(videoId: String) -> Bool {
        let fileManager = FileManager.default
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
        let fileURL = documentsURL.appendingPathComponent(videoId).appendingPathExtension("mp4")
        return fileManager.fileExists(atPath: fileURL.path)
    }
    
    func getLocalURL(for videoId: String) -> URL? {
        let fileManager = FileManager.default
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
        let fileURL = documentsURL.appendingPathComponent(videoId).appendingPathExtension("mp4")
        return fileManager.fileExists(atPath: fileURL.path) ? fileURL : nil
    }
    
    // MARK: - URLSessionDownloadDelegate
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didFinishDownloadingTo location: URL) {
        guard let originalURL = downloadTask.originalRequest?.url,
              let downloadTaskInfo = activeDownloads[originalURL] else { return }
        
        let fileManager = FileManager.default
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
        let destinationURL = documentsURL.appendingPathComponent(downloadTaskInfo.videoId).appendingPathExtension("mp4")
        
        do {
            if fileManager.fileExists(atPath: destinationURL.path) {
                try fileManager.removeItem(at: destinationURL)
            }
            try fileManager.moveItem(at: location, to: destinationURL)
            var updated = downloadTaskInfo
            updated.localURL = destinationURL
            updated.isDownloading = false
            updated.progress = 1.0
            downloads[downloadTaskInfo.videoId] = updated
            activeDownloads.removeValue(forKey: originalURL)
        } catch {
            print("Download save error: \\(error)")
        }
    }
    
    func urlSession(_ session: URLSession, downloadTask: URLSessionDownloadTask, didWriteData bytesWritten: Int64, totalBytesWritten: Int64, totalBytesExpectedToWrite: Int64) {
        let progress = Double(totalBytesWritten) / Double(totalBytesExpectedToWrite)
        guard let originalURL = downloadTask.originalRequest?.url,
              var downloadTaskInfo = activeDownloads[originalURL] else { return }
        downloadTaskInfo.progress = progress
        downloads[downloadTaskInfo.videoId] = downloadTaskInfo
    }
}
"""

with open("UTan/UTan/DownloadManager.swift", "w", encoding="utf-8") as f:
    f.write(download_manager_swift)

# 7. Write Scraper.swift (محدث ليشمل جميع الصفحات والتفاصيل)
scraper_swift = """import Foundation
import SwiftUI

class MovieScraper: ObservableObject {
    @Published var isLoading = false
    @Published var heroItems: [VideoItem] = []
    @Published var categories: [String: [VideoItem]] = [:]
    @Published var allItemsPool: [VideoItem] = []
    @Published var searchResults: [VideoItem] = []
    
    let baseUrl = "https://movie.vodu.me/"
    
    // MARK: - Home Page
    func fetchHome() {
        guard let url = URL(string: baseUrl + "index.php") else { return }
        isLoading = true
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                DispatchQueue.main.async { self.isLoading = false }
                return
            }
            
            // Parse carousel items (from div id="myCarousel")
            var carouselItems: [VideoItem] = []
            let carouselPattern = #"<div class="item[^>]*>\\s*<a href="index\.php\\?do=view&type=post&id=(\\d+)".*?<img src="([^"]+)".*?alt="([^"]+)"#s
            if let regex = try? NSRegularExpression(pattern: carouselPattern, options: []) {
                let nsRange = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: nsRange)
                for match in matches {
                    if match.numberOfRanges >= 4,
                       let idRange = Range(match.range(at: 1), in: html),
                       let imgRange = Range(match.range(at: 2), in: html),
                       let titleRange = Range(match.range(at: 3), in: html) {
                        let id = String(html[idRange])
                        var img = String(html[imgRange])
                        if !img.hasPrefix("http") { img = self.baseUrl + img }
                        let title = String(html[titleRange])
                        carouselItems.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
            
            // Parse category rows: each row has h2 with link and then div class="homeseries"
            var newCategories: [String: [VideoItem]] = [:]
            let categoryBlockPattern = #"<div class="col-lg-12">\\s*<h2><a href="[^"]+">([^<]+)</a></h2>.*?<div class="homeseries">(.*?)</div>\\s*</div>"#s
            if let catRegex = try? NSRegularExpression(pattern: categoryBlockPattern, options: []) {
                let nsRange = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = catRegex.matches(in: html, options: [], range: nsRange)
                for match in matches {
                    if match.numberOfRanges >= 3,
                       let nameRange = Range(match.range(at: 1), in: html),
                       let contentRange = Range(match.range(at: 2), in: html) {
                        let catName = String(html[nameRange]).trimmingCharacters(in: .whitespacesAndNewlines)
                        let content = String(html[contentRange])
                        var items: [VideoItem] = []
                        let itemPattern = #"<a href="index\.php\\?do=view&type=post&id=(\\d+)">.*?<img src="([^"]+)".*?<div class="mytitle">([^<]+)</div>"#s
                        if let itemRegex = try? NSRegularExpression(pattern: itemPattern, options: []) {
                            let itemNsRange = NSRange(content.startIndex..<content.endIndex, in: content)
                            let itemMatches = itemRegex.matches(in: content, options: [], range: itemNsRange)
                            for itemMatch in itemMatches {
                                if itemMatch.numberOfRanges >= 4,
                                   let idRange = Range(itemMatch.range(at: 1), in: content),
                                   let imgRange = Range(itemMatch.range(at: 2), in: content),
                                   let titleRange = Range(itemMatch.range(at: 3), in: content) {
                                    let id = String(content[idRange])
                                    var img = String(content[imgRange])
                                    if !img.hasPrefix("http") { img = self.baseUrl + img }
                                    let title = String(content[titleRange])
                                    items.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                                }
                            }
                        }
                        if !items.isEmpty {
                            newCategories[catName] = items
                            self.allItemsPool.append(contentsOf: items)
                        }
                    }
                }
            }
            
            DispatchQueue.main.async {
                self.isLoading = false
                self.heroItems = carouselItems
                self.categories = newCategories
            }
        }.resume()
    }
    
    // MARK: - Category Listing (with pagination and sorting)
    func fetchCategory(type: String, page: Int = 1, sort: String = "date", genre: String = "", completion: @escaping ([VideoItem], Int) -> Void) {
        var urlString = baseUrl + "index.php?do=list&type=\\(type)&page=\\(page)&sort=\\(sort)"
        if !genre.isEmpty {
            urlString += "&genre=\\(genre.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? "")"
        }
        guard let url = URL(string: urlString) else { return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                completion([], 0)
                return
            }
            var items: [VideoItem] = []
            let pattern = #"<li class="animated[^>]*>.*?<a href="index\.php\\?do=view&type=post&id=(\\d+)".*?<img src="([^"]+)".*?<div class="mytitle">\\s*<a[^>]*>([^<]+)</a>"#s
            if let regex = try? NSRegularExpression(pattern: pattern, options: []) {
                let nsRange = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: nsRange)
                for match in matches {
                    if match.numberOfRanges >= 4,
                       let idRange = Range(match.range(at: 1), in: html),
                       let imgRange = Range(match.range(at: 2), in: html),
                       let titleRange = Range(match.range(at: 3), in: html) {
                        let id = String(html[idRange])
                        var img = String(html[imgRange])
                        if !img.hasPrefix("http") { img = self.baseUrl + img }
                        let title = String(html[titleRange])
                        items.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
            // Parse total pages from pagination
            var totalPages = 1
            let pagePattern = #"<li><a href="[^"]*page=(\\d+)"#s
            if let regex = try? NSRegularExpression(pattern: pagePattern, options: []) {
                let nsRange = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: nsRange)
                if let lastMatch = matches.last, let range = Range(lastMatch.range(at: 1), in: html) {
                    totalPages = Int(html[range]) ?? 1
                }
            }
            DispatchQueue.main.async {
                completion(items, totalPages)
            }
        }.resume()
    }
    
    // MARK: - Search
    func search(query: String, completion: @escaping ([VideoItem]) -> Void) {
        guard let url = URL(string: baseUrl + "index.php?do=list&title=\\(query.addingPercentEncoding(withAllowedCharacters: .urlQueryAllowed) ?? "")") else { return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                completion([])
                return
            }
            var items: [VideoItem] = []
            let pattern = #"<div class="myitem">.*?<a href="index\.php\\?do=view&type=post&id=(\\d+)".*?<img src="([^"]+)".*?<div class="mytitle">\\s*<a[^>]*>([^<]+)</a>"#s
            if let regex = try? NSRegularExpression(pattern: pattern, options: [.dotMatchesLineSeparators]) {
                let nsRange = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: nsRange)
                for match in matches {
                    if match.numberOfRanges >= 4,
                       let idRange = Range(match.range(at: 1), in: html),
                       let imgRange = Range(match.range(at: 2), in: html),
                       let titleRange = Range(match.range(at: 3), in: html) {
                        let id = String(html[idRange])
                        var img = String(html[imgRange])
                        if !img.hasPrefix("http") { img = self.baseUrl + img }
                        let title = String(html[titleRange])
                        items.append(VideoItem(id: id, title: title, imageUrl: img, type: "post"))
                    }
                }
            }
            DispatchQueue.main.async {
                completion(items)
            }
        }.resume()
    }
    
    // MARK: - Details Page (Movie or Series)
    func fetchDetails(id: String, completion: @escaping (MediaDetails) -> Void) {
        guard let url = URL(string: baseUrl + "index.php?do=view&type=post&id=\\(id)") else { return }
        URLSession.shared.dataTask(with: url) { data, _, _ in
            var details = MediaDetails()
            details.id = id
            guard let data = data, let html = String(data: data, encoding: .utf8) else {
                completion(details)
                return
            }
            
            // Title
            if let titleRegex = try? NSRegularExpression(pattern: #"<h1>(.*?)</h1>"#, options: []),
               let match = titleRegex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)),
               let range = Range(match.range(at: 1), in: html) {
                details.title = String(html[range]).trimmingCharacters(in: .whitespacesAndNewlines)
            }
            
            // Synopsis
            let synPattern = #"<h3>Synopsis:</h3>\\s*<h4>(.*?)</h4>"#s
            if let regex = try? NSRegularExpression(pattern: synPattern, options: []),
               let match = regex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)),
               let range = Range(match.range(at: 1), in: html) {
                details.synopsis = String(html[range]).trimmingCharacters(in: .whitespacesAndNewlines)
            }
            
            // Metadata
            let metadataKeys: [String: String] = [
                "year": #"<span>Year: </span>\\s*([^<]+)"#,
                "genre": #"<span>Genre: </span>\\s*([^<]+)"#,
                "rating": #"<span>IMdB Rating: </span>\\s*([^<]+)"#,
                "runtime": #"<span>Runtime:\\s*</span>\\s*([^<]+)"#
            ]
            for (key, pattern) in metadataKeys {
                if let regex = try? NSRegularExpression(pattern: pattern, options: []),
                   let match = regex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)),
                   let range = Range(match.range(at: 1), in: html) {
                    let value = String(html[range]).trimmingCharacters(in: .whitespacesAndNewlines)
                    if key == "year" { details.year = value }
                    if key == "genre" { details.genre = value }
                    if key == "rating" { details.rating = value }
                    if key == "runtime" { details.runtime = value }
                }
            }
            
            // Image
            if let imgRegex = try? NSRegularExpression(pattern: #"<img src="([^"]+)" class="img-responsive""#, options: []),
               let match = imgRegex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)),
               let range = Range(match.range(at: 1), in: html) {
                var img = String(html[range])
                if !img.hasPrefix("http") { img = self.baseUrl + img }
                details.imageUrl = img
            }
            
            // Parse episodes (for series)
            var episodes: [EpisodeItem] = []
            let epPattern = #"data-srt="([^"]*)"[^>]*data-id="(\\d+)"[^>]*data-title="([^"]*)"\\s*data-url="([^"]*)"[^>]*data-url360="([^"]*)"\\s*data-url1080="([^"]*)"\\s*data-url4k="([^"]*)"#s
            if let regex = try? NSRegularExpression(pattern: epPattern, options: []) {
                let nsRange = NSRange(html.startIndex..<html.endIndex, in: html)
                let matches = regex.matches(in: html, options: [], range: nsRange)
                for match in matches {
                    if match.numberOfRanges >= 8,
                       let srtRange = Range(match.range(at: 1), in: html),
                       let idRange = Range(match.range(at: 2), in: html),
                       let titleRange = Range(match.range(at: 3), in: html),
                       let urlRange = Range(match.range(at: 4), in: html),
                       let url360Range = Range(match.range(at: 5), in: html),
                       let url1080Range = Range(match.range(at: 6), in: html),
                       let url4kRange = Range(match.range(at: 7), in: html) {
                        let ep = EpisodeItem(
                            id: String(html[idRange]),
                            title: String(html[titleRange]).isEmpty ? "Episode \\(episodes.count+1)" : String(html[titleRange]),
                            url: String(html[urlRange]),
                            url360: String(html[url360Range]),
                            url1080: String(html[url1080Range]),
                            url4k: String(html[url4kRange]),
                            subtitleUrl: String(html[srtRange])
                        )
                        episodes.append(ep)
                    }
                }
            }
            
            if episodes.isEmpty {
                // It's a movie: get single video URLs
                details.isMovie = true
                let movieUrlPattern = #"data-url="([^"]+)".*?data-url360="([^"]+)".*?data-url1080="([^"]+)".*?data-url4k="([^"]+)".*?data-srt="([^"]*)"#s
                if let regex = try? NSRegularExpression(pattern: movieUrlPattern, options: []),
                   let match = regex.firstMatch(in: html, options: [], range: NSRange(html.startIndex..<html.endIndex, in: html)) {
                    if match.numberOfRanges >= 6 {
                        if let urlRange = Range(match.range(at: 1), in: html) { details.movieUrl = String(html[urlRange]) }
                        if let url360Range = Range(match.range(at: 2), in: html) { details.movieUrl360 = String(html[url360Range]) }
                        if let url1080Range = Range(match.range(at: 3), in: html) { details.movieUrl1080 = String(html[url1080Range]) }
                        if let url4kRange = Range(match.range(at: 4), in: html) { details.movieUrl4k = String(html[url4kRange]) }
                        if let srtRange = Range(match.range(at: 5), in: html) { details.movieSubtitleUrl = String(html[srtRange]) }
                    }
                }
            } else {
                details.isMovie = false
                details.episodes = episodes
            }
            
            // Parse similar items
            var similar: [VideoItem] = []
            let similarPattern = #"<div class="homeseries">(.*?)</div>\\s*</div>\\s*</div>\\s*<div class="row">"#s
            if let similarBlockRange = html.range(of: similarPattern, options: .regularExpression),
               let similarRegex = try? NSRegularExpression(pattern: #"<a href="index\.php\\?do=view&type=post&id=(\\d+)".*?<img src="([^"]+)".*?<div class="mytitle">([^<]+)</div>"#, options: [.dotMatchesLineSeparators]) {
                let similarBlock = String(html[similarBlockRange])
                let nsRange = NSRange(similarBlock.startIndex..<similarBlock.endIndex, in: similarBlock)
                let matches = similarRegex.matches(in: similarBlock, options: [], range: nsRange)
                for match in matches {
                    if match.numberOfRanges >= 4,
                       let idRange = Range(match.range(at: 1), in: similarBlock),
                       let imgRange = Range(match.range(at: 2), in: similarBlock),
                       let titleRange = Range(match.range(at: 3), in: similarBlock) {
                        let sid = String(similarBlock[idRange])
                        var img = String(similarBlock[imgRange])
                        if !img.hasPrefix("http") { img = self.baseUrl + img }
                        let stitle = String(similarBlock[titleRange])
                        similar.append(VideoItem(id: sid, title: stitle, imageUrl: img, type: "post"))
                    }
                }
            }
            details.similarItems = similar
            
            DispatchQueue.main.async {
                completion(details)
            }
        }.resume()
    }
}
"""

with open("UTan/UTan/Scraper.swift", "w", encoding="utf-8") as f:
    f.write(scraper_swift)

# 8. Write SubtitleParser.swift (محدث للتعامل مع WebVTT)
sub_parser_swift = """import Foundation

struct SubtitleCue: Identifiable {
    let id = UUID()
    let startTime: TimeInterval
    let endTime: TimeInterval
    let text: String
}

class SubtitleParser {
    static func parse(url: String, completion: @escaping ([SubtitleCue]) -> Void) {
        guard !url.isEmpty, let urlObj = URL(string: url.hasPrefix("http") ? url : "https://movie.vodu.me/" + url) else {
            completion([])
            return
        }
        URLSession.shared.dataTask(with: urlObj) { data, _, _ in
            guard let data = data, let content = String(data: data, encoding: .utf8) else {
                completion([])
                return
            }
            let cues = parseWebVTT(content)
            DispatchQueue.main.async {
                completion(cues)
            }
        }.resume()
    }
    
    private static func parseWebVTT(_ content: String) -> [SubtitleCue] {
        var cues: [SubtitleCue] = []
        let lines = content.components(separatedBy: .newlines)
        var currentStart: TimeInterval?
        var currentEnd: TimeInterval?
        var currentText = ""
        
        for line in lines {
            let trimmed = line.trimmingCharacters(in: .whitespaces)
            if trimmed.isEmpty {
                if let start = currentStart, let end = currentEnd, !currentText.isEmpty {
                    cues.append(SubtitleCue(startTime: start, endTime: end, text: currentText.trimmingCharacters(in: .whitespacesAndNewlines)))
                }
                currentStart = nil
                currentEnd = nil
                currentText = ""
                continue
            }
            
            if trimmed.contains("-->") {
                let parts = trimmed.components(separatedBy: "-->")
                if parts.count >= 2 {
                    currentStart = parseTimeString(parts[0])
                    currentEnd = parseTimeString(parts[1])
                }
            } else if !trimmed.hasPrefix("WEBVTT") && !trimmed.hasPrefix("Kind:") && !trimmed.hasPrefix("Language:") && !trimmed.allSatisfy({ $0.isNumber || $0 == "." }) {
                if currentText.isEmpty {
                    currentText = trimmed
                } else {
                    currentText += "\\n" + trimmed
                }
            }
        }
        
        if let start = currentStart, let end = currentEnd, !currentText.isEmpty {
            cues.append(SubtitleCue(startTime: start, endTime: end, text: currentText))
        }
        return cues
    }
    
    private static func parseTimeString(_ timeStr: String) -> TimeInterval? {
        let clean = timeStr.trimmingCharacters(in: .whitespaces).replacingOccurrences(of: ",", with: ".")
        let components = clean.components(separatedBy: ":")
        var hours: Double = 0, minutes: Double = 0, seconds: Double = 0
        if components.count == 3 {
            hours = Double(components[0]) ?? 0
            minutes = Double(components[1]) ?? 0
            seconds = Double(components[2]) ?? 0
        } else if components.count == 2 {
            minutes = Double(components[0]) ?? 0
            seconds = Double(components[1]) ?? 0
        }
        return (hours * 3600) + (minutes * 60) + seconds
    }
}
"""

with open("UTan/UTan/SubtitleParser.swift", "w", encoding="utf-8") as f:
    f.write(sub_parser_swift)

# 9. Write CustomPlayerView.swift (محدث بشكل كامل مع ضغطة مطولة، جودة، تحميل)
player_swift = """import SwiftUI
import AVKit
import CoreData

struct CustomPlayerView: View {
    let videoId: String
    let title: String
    let imageUrl: String
    let subtitleUrl: String
    let videoUrls: [VideoQuality: String] // quality -> url
    
    @Environment(\\.presentationMode) var presentationMode
    @State private var player: AVPlayer?
    @State private var isPlaying = true
    @State private var currentTime: TimeInterval = 0
    @State private var duration: TimeInterval = 0
    @State private var cues: [SubtitleCue] = []
    @State private var activeSubtitleText = ""
    @State private var isLocked = false
    @State private var fitMode: VideoFitMode = .fit
    @State private var currentQuality: VideoQuality = .p720
    @State private var showSettings = false
    @State private var showControls = true
    @State private var controlsTimer: Timer?
    @State private var timeObserver: Any?
    
    @State private var fontSize: CGFloat = 22
    @State private var verticalOffset: CGFloat = 50
    
    let qualities: [VideoQuality] = [.p360, .p720, .p1080, .p4K]
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            if let player = player {
                VideoPlayerRepresentable(player: player, gravity: fitMode.gravity)
                    .ignoresSafeArea()
                    .onTapGesture {
                        // Single tap: toggle controls
                        withAnimation {
                            showControls.toggle()
                        }
                        resetControlsTimer()
                    }
                    .onLongPressGesture(minimumDuration: 0.5) {
                        // Long press: speed up to 2x
                        player.rate = 2.0
                        DispatchQueue.main.asyncAfter(deadline: .now() + 0.3) {
                            if player.rate == 2.0 && isPlaying {
                                player.rate = Float(currentSpeed())
                            }
                        }
                    }
                
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
                    .allowsHitTesting(false)
                }
                
                if showControls {
                    VStack {
                        HStack {
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
                                Menu {
                                    ForEach(qualities, id: \\.self) { quality in
                                        if let _ = videoUrls[quality] {
                                            Button(action: {
                                                switchQuality(to: quality)
                                            }) {
                                                HStack {
                                                    Text(quality.rawValue)
                                                    if currentQuality == quality {
                                                        Image(systemName: "checkmark")
                                                    }
                                                }
                                            }
                                        }
                                    }
                                } label: {
                                    Image(systemName: "hifispeaker.fill")
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
                                
                                Button(action: {
                                    DownloadManager.shared.startDownload(videoId: videoId, title: title, imageUrl: imageUrl, quality: currentQuality, videoURL: URL(string: videoUrls[currentQuality] ?? "")!)
                                }) {
                                    Image(systemName: DownloadManager.shared.isDownloaded(videoId: videoId) ? "arrow.down.circle.fill" : "arrow.down.circle")
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
                                            player.rate = Float(currentSpeed())
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
        }
        .statusBar(hidden: true)
        .onAppear {
            setupPlayer()
            loadSavedProgress()
        }
        .onDisappear {
            saveProgress()
            shutdownPlayer()
        }
        .sheet(isPresented: $showSettings) {
            SettingsView(fontSize: $fontSize, verticalOffset: $verticalOffset, player: player)
        }
    }
    
    private func setupPlayer() {
        guard let urlString = videoUrls[currentQuality], let url = URL(string: urlString) else { return }
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
    
    private func switchQuality(to quality: VideoQuality) {
        guard let urlString = videoUrls[quality], let url = URL(string: urlString) else { return }
        let wasPlaying = isPlaying
        let currentTime = self.currentTime
        let newPlayerItem = AVPlayerItem(url: url)
        player?.replaceCurrentItem(with: newPlayerItem)
        player?.seek(to: CMTime(seconds: currentTime, preferredTimescale: 600))
        if wasPlaying {
            player?.play()
            player?.rate = Float(currentSpeed())
        }
        currentQuality = quality
    }
    
    private func currentSpeed() -> Double {
        // يمكنك إضافة سرعة مخصصة من الإعدادات لاحقاً
        return 1.0
    }
    
    private func loadSavedProgress() {
        let context = PersistenceController.shared.container.viewContext
        let request = NSFetchRequest<NSManagedObject>(entityName: "WatchHistory")
        request.predicate = NSPredicate(format: "videoId == %@", videoId)
        if let result = try? context.fetch(request).first,
           let timestamp = result.value(forKey: "timestamp") as? Double {
            currentTime = timestamp
        }
    }
    
    private func saveProgress() {
        let context = PersistenceController.shared.container.viewContext
        let request = NSFetchRequest<NSManagedObject>(entityName: "WatchHistory")
        request.predicate = NSPredicate(format: "videoId == %@", videoId)
        if let existing = try? context.fetch(request).first {
            existing.setValue(currentTime, forKey: "timestamp")
        } else {
            let entity = NSEntityDescription.entity(forEntityName: "WatchHistory", in: context)!
            let new = NSManagedObject(entity: entity, insertInto: context)
            new.setValue(videoId, forKey: "videoId")
            new.setValue(title, forKey: "title")
            new.setValue(imageUrl, forKey: "imageUrl")
            new.setValue(currentTime, forKey: "timestamp")
            new.setValue(duration, forKey: "duration")
        }
        try? context.save()
    }
    
    private func shutdownPlayer() {
        if let observer = timeObserver {
            player?.removeTimeObserver(observer)
            timeObserver = nil
        }
        player?.pause()
        player = nil
        controlsTimer?.invalidate()
    }
    
    private func resetControlsTimer() {
        controlsTimer?.invalidate()
        controlsTimer = Timer.scheduledTimer(withTimeInterval: 3.0, repeats: false) { _ in
            withAnimation {
                showControls = false
            }
        }
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

enum VideoFitMode: String, CaseIterable, Identifiable {
    case fit = "Fit"
    case fill = "Stretch"
    case zoom = "Crop"
    var id: String { self.rawValue }
    var gravity: AVLayerVideoGravity {
        switch self {
        case .fit: return .resizeAspect
        case .fill: return .resize
        case .zoom: return .resizeAspectFill
        }
    }
}

struct SettingsView: View {
    @Binding var fontSize: CGFloat
    @Binding var verticalOffset: CGFloat
    var player: AVPlayer?
    @Environment(\\.presentationMode) var presentationMode
    
    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Subtitle Size")) {
                    Slider(value: $fontSize, in: 16...36, step: 1)
                    Text("Font: \\(Int(fontSize)) pt")
                }
                Section(header: Text("Vertical Position")) {
                    Slider(value: $verticalOffset, in: 20...160, step: 5)
                    Text("Offset: \\(Int(verticalOffset)) px")
                }
            }
            .navigationTitle("Player Settings")
            .navigationBarItems(trailing: Button("Done") {
                presentationMode.wrappedValue.dismiss()
            })
        }
    }
}
"""

with open("UTan/UTan/CustomPlayerView.swift", "w", encoding="utf-8") as f:
    f.write(player_swift)

# 10. Write HomeView.swift (مع قسم متابعة المشاهدة)
home_swift = """import SwiftUI
import CoreData

struct HomeView: View {
    @StateObject private var scraper = MovieScraper()
    @State private var searchText = ""
    @State private var showingSearch = false
    @Environment(\\.managedObjectContext) private var viewContext
    
    @FetchRequest(
        entity: NSManagedObject.entity(forEntityName: "WatchHistory")!,
        sortDescriptors: [NSSortDescriptor(keyPath: \NSManagedObject.value(forKey: "timestamp"), ascending: false)],
        predicate: NSPredicate(format: "timestamp > 0")
    ) var watchHistory: FetchedResults<NSManagedObject>
    
    var body: some View {
        NavigationView {
            ZStack {
                Color.black.ignoresSafeArea()
                
                if scraper.isLoading {
                    ProgressView()
                        .progressViewStyle(CircularProgressViewStyle(tint: .white))
                        .scaleEffect(1.5)
                } else {
                    ScrollView {
                        VStack(alignment: .leading, spacing: 20) {
                            // Carousel
                            if !scraper.heroItems.isEmpty {
                                TabView {
                                    ForEach(scraper.heroItems) { item in
                                        NavigationLink(destination: DetailsView(itemId: item.id)) {
                                            AsyncImage(url: URL(string: item.imageUrl)) { img in
                                                img.resizable().aspectRatio(contentMode: .fill)
                                            } placeholder: {
                                                Color.gray
                                            }
                                            .frame(height: 400)
                                            .clipped()
                                            .overlay(
                                                LinearGradient(colors: [.clear, .black.opacity(0.7)], startPoint: .top, endPoint: .bottom)
                                            )
                                            .overlay(
                                                Text(item.title)
                                                    .font(.title2)
                                                    .bold()
                                                    .foregroundColor(.white)
                                                    .padding()
                                                    .frame(maxWidth: .infinity, alignment: .bottomLeading),
                                                alignment: .bottomLeading
                                            )
                                        }
                                    }
                                }
                                .frame(height: 400)
                                .tabViewStyle(PageTabViewStyle(indexDisplayMode: .automatic))
                            }
                            
                            // Continue Watching Section
                            if !watchHistory.isEmpty {
                                VStack(alignment: .leading, spacing: 8) {
                                    Text("Continue Watching")
                                        .font(.title2)
                                        .bold()
                                        .foregroundColor(.white)
                                        .padding(.horizontal)
                                    
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 12) {
                                            ForEach(watchHistory, id: \\.self) { item in
                                                let videoId = item.value(forKey: "videoId") as? String ?? ""
                                                let title = item.value(forKey: "title") as? String ?? ""
                                                let imageUrl = item.value(forKey: "imageUrl") as? String ?? ""
                                                let timestamp = item.value(forKey: "timestamp") as? Double ?? 0
                                                let duration = item.value(forKey: "duration") as? Double ?? 1
                                                let progress = timestamp / duration
                                                
                                                NavigationLink(destination: DetailsView(itemId: videoId)) {
                                                    VStack(alignment: .leading) {
                                                        AsyncImage(url: URL(string: imageUrl)) { img in
                                                            img.resizable().aspectRatio(contentMode: .fill)
                                                        } placeholder: {
                                                            Color.gray
                                                        }
                                                        .frame(width: 120, height: 180)
                                                        .cornerRadius(8)
                                                        .overlay(
                                                            VStack {
                                                                Spacer()
                                                                ProgressView(value: progress, total: 1.0)
                                                                    .progressViewStyle(LinearProgressViewStyle(tint: Color.red))
                                                                    .padding(.horizontal, 4)
                                                                    .padding(.bottom, 4)
                                                            }
                                                        )
                                                        
                                                        Text(title)
                                                            .font(.caption)
                                                            .foregroundColor(.white)
                                                            .lineLimit(1)
                                                            .frame(width: 120)
                                                    }
                                                }
                                            }
                                        }
                                        .padding(.horizontal)
                                    }
                                }
                            }
                            
                            // Categories
                            ForEach(scraper.categories.keys.sorted(), id: \\.self) { catName in
                                VStack(alignment: .leading, spacing: 8) {
                                    HStack {
                                        Text(catName)
                                            .font(.title2)
                                            .bold()
                                            .foregroundColor(.white)
                                        Spacer()
                                        NavigationLink(destination: CategoryListView(type: "all", title: catName, initialItems: scraper.categories[catName] ?? [])) {
                                            Text("View All")
                                                .font(.subheadline)
                                                .foregroundColor(Color.red)
                                        }
                                    }
                                    .padding(.horizontal)
                                    
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 12) {
                                            ForEach(scraper.categories[catName] ?? []) { item in
                                                NavigationLink(destination: DetailsView(itemId: item.id)) {
                                                    VStack(alignment: .leading) {
                                                        AsyncImage(url: URL(string: item.imageUrl)) { img in
                                                            img.resizable().aspectRatio(contentMode: .fill)
                                                        } placeholder: {
                                                            Color.gray
                                                        }
                                                        .frame(width: 120, height: 180)
                                                        .cornerRadius(8)
                                                        
                                                        Text(item.title)
                                                            .font(.caption)
                                                            .foregroundColor(.white)
                                                            .lineLimit(1)
                                                            .frame(width: 120)
                                                    }
                                                }
                                            }
                                        }
                                        .padding(.horizontal)
                                    }
                                }
                            }
                        }
                        .padding(.bottom, 20)
                    }
                }
            }
            .navigationBarHidden(true)
            .searchable(text: $searchText, prompt: "Search movies or series")
            .onSubmit(of: .search) {
                if !searchText.isEmpty {
                    showingSearch = true
                }
            }
            .sheet(isPresented: $showingSearch) {
                SearchView(query: searchText)
            }
        }
        .onAppear {
            if scraper.categories.isEmpty {
                scraper.fetchHome()
            }
        }
    }
}
"""

with open("UTan/UTan/HomeView.swift", "w", encoding="utf-8") as f:
    f.write(home_swift)

# 11. Write SearchView.swift
search_swift = """import SwiftUI

struct SearchView: View {
    let query: String
    @StateObject private var scraper = MovieScraper()
    @State private var results: [VideoItem] = []
    @State private var isLoading = true
    @Environment(\\.presentationMode) var presentationMode
    
    var body: some View {
        NavigationView {
            ZStack {
                Color.black.ignoresSafeArea()
                if isLoading {
                    ProgressView()
                        .progressViewStyle(CircularProgressViewStyle(tint: .white))
                } else {
                    ScrollView {
                        LazyVGrid(columns: [GridItem(.adaptive(minimum: 120), spacing: 12)], spacing: 16) {
                            ForEach(results) { item in
                                NavigationLink(destination: DetailsView(itemId: item.id)) {
                                    VStack {
                                        AsyncImage(url: URL(string: item.imageUrl)) { img in
                                            img.resizable().aspectRatio(contentMode: .fill)
                                        } placeholder: {
                                            Color.gray
                                        }
                                        .frame(width: 120, height: 180)
                                        .cornerRadius(8)
                                        Text(item.title)
                                            .font(.caption)
                                            .foregroundColor(.white)
                                            .lineLimit(1)
                                            .frame(width: 120)
                                    }
                                }
                            }
                        }
                        .padding()
                    }
                }
            }
            .navigationTitle("Search: \\(query)")
            .navigationBarItems(trailing: Button("Close") {
                presentationMode.wrappedValue.dismiss()
            })
        }
        .onAppear {
            scraper.search(query: query) { items in
                results = items
                isLoading = false
            }
        }
    }
}
"""

with open("UTan/UTan/SearchView.swift", "w", encoding="utf-8") as f:
    f.write(search_swift)

# 12. Write CategoryListView.swift
category_list_swift = """import SwiftUI

struct CategoryListView: View {
    let type: String
    let title: String
    let initialItems: [VideoItem]
    @State private var items: [VideoItem] = []
    @State private var currentPage = 1
    @State private var totalPages = 1
    @State private var isLoading = false
    @State private var sortOption = "date"
    @State private var selectedGenre = ""
    @StateObject private var scraper = MovieScraper()
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            VStack {
                // Sorting and filtering toolbar
                ScrollView(.horizontal, showsIndicators: false) {
                    HStack {
                        Button("Upload Date") { sortOption = "date"; loadPage(reset: true) }
                            .foregroundColor(sortOption == "date" ? .red : .white)
                        Button("Year") { sortOption = "year"; loadPage(reset: true) }
                            .foregroundColor(sortOption == "year" ? .red : .white)
                        Button("Rating") { sortOption = "rating"; loadPage(reset: true) }
                            .foregroundColor(sortOption == "rating" ? .red : .white)
                        Button("Views") { sortOption = "views"; loadPage(reset: true) }
                            .foregroundColor(sortOption == "views" ? .red : .white)
                    }
                    .padding(.horizontal)
                }
                .padding(.vertical, 8)
                
                ScrollView {
                    LazyVGrid(columns: [GridItem(.adaptive(minimum: 120), spacing: 12)], spacing: 16) {
                        ForEach(items) { item in
                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                VStack {
                                    AsyncImage(url: URL(string: item.imageUrl)) { img in
                                        img.resizable().aspectRatio(contentMode: .fill)
                                    } placeholder: {
                                        Color.gray
                                    }
                                    .frame(width: 120, height: 180)
                                    .cornerRadius(8)
                                    Text(item.title)
                                        .font(.caption)
                                        .foregroundColor(.white)
                                        .lineLimit(1)
                                        .frame(width: 120)
                                }
                            }
                        }
                    }
                    .padding()
                    
                    if currentPage < totalPages {
                        Button("Load More") {
                            currentPage += 1
                            loadPage()
                        }
                        .padding()
                        .foregroundColor(.red)
                    }
                    
                    if isLoading {
                        ProgressView()
                            .progressViewStyle(CircularProgressViewStyle(tint: .white))
                    }
                }
            }
        }
        .navigationTitle(title)
        .onAppear {
            if items.isEmpty {
                items = initialItems
                loadPage(reset: true)
            }
        }
    }
    
    private func loadPage(reset: Bool = false) {
        if reset {
            currentPage = 1
            items = []
        }
        isLoading = true
        scraper.fetchCategory(type: type, page: currentPage, sort: sortOption, genre: selectedGenre) { newItems, total in
            if reset {
                items = newItems
            } else {
                items.append(contentsOf: newItems)
            }
            totalPages = total
            isLoading = false
        }
    }
}
"""

with open("UTan/UTan/CategoryListView.swift", "w", encoding="utf-8") as f:
    f.write(category_list_swift)

# 13. Write DetailsView.swift (شاشة التفاصيل الكاملة)
details_swift = """import SwiftUI

struct DetailsView: View {
    let itemId: String
    @StateObject private var scraper = MovieScraper()
    @State private var details: MediaDetails?
    @State private var isLoading = true
    @State private var selectedQuality: VideoQuality = .p720
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            if isLoading {
                ProgressView()
                    .progressViewStyle(CircularProgressViewStyle(tint: .white))
            } else if let details = details {
                ScrollView {
                    VStack(alignment: .leading, spacing: 16) {
                        // Header poster
                        AsyncImage(url: URL(string: details.imageUrl)) { img in
                            img.resizable().aspectRatio(contentMode: .fill)
                        } placeholder: {
                            Color.gray
                        }
                        .frame(height: 300)
                        .clipped()
                        .overlay(
                            LinearGradient(colors: [.clear, .black.opacity(0.8)], startPoint: .top, endPoint: .bottom)
                        )
                        
                        VStack(alignment: .leading, spacing: 12) {
                            Text(details.title)
                                .font(.largeTitle)
                                .bold()
                                .foregroundColor(.white)
                            
                            HStack(spacing: 16) {
                                Text(details.year)
                                    .font(.subheadline)
                                Text(details.rating)
                                    .font(.subheadline)
                                    .foregroundColor(.yellow)
                                Text(details.runtime)
                                    .font(.subheadline)
                            }
                            
                            Text(details.genre)
                                .font(.subheadline)
                                .foregroundColor(.gray)
                            
                            Text(details.synopsis)
                                .font(.body)
                                .foregroundColor(.white.opacity(0.8))
                                .padding(.top, 4)
                            
                            if details.isMovie {
                                // Movie player button with quality selection
                                if let movieUrl = getMovieUrl(for: selectedQuality), !movieUrl.isEmpty {
                                    NavigationLink(destination: CustomPlayerView(
                                        videoId: itemId,
                                        title: details.title,
                                        imageUrl: details.imageUrl,
                                        subtitleUrl: details.movieSubtitleUrl,
                                        videoUrls: getQualityMap()
                                    )) {
                                        HStack {
                                            Image(systemName: "play.fill")
                                            Text("Play Now")
                                        }
                                        .frame(maxWidth: .infinity)
                                        .padding()
                                        .background(Color.red)
                                        .foregroundColor(.white)
                                        .cornerRadius(8)
                                    }
                                    
                                    // Quality picker
                                    Picker("Quality", selection: $selectedQuality) {
                                        ForEach(Array(getQualityMap().keys), id: \\.self) { quality in
                                            Text(quality.rawValue).tag(quality)
                                        }
                                    }
                                    .pickerStyle(SegmentedPickerStyle())
                                    .padding(.top, 4)
                                }
                            } else {
                                // Episodes list
                                Text("Episodes")
                                    .font(.title2)
                                    .bold()
                                    .foregroundColor(.white)
                                    .padding(.top, 8)
                                
                                ForEach(details.episodes) { episode in
                                    NavigationLink(destination: CustomPlayerView(
                                        videoId: episode.id,
                                        title: episode.title,
                                        imageUrl: details.imageUrl,
                                        subtitleUrl: episode.subtitleUrl,
                                        videoUrls: [
                                            .p360: episode.url360,
                                            .p720: episode.url,
                                            .p1080: episode.url1080,
                                            .p4K: episode.url4k
                                        ].compactMapValues { $0 }
                                    )) {
                                        HStack {
                                            Image(systemName: "play.rectangle.fill")
                                                .foregroundColor(.red)
                                            Text(episode.title)
                                                .foregroundColor(.white)
                                            Spacer()
                                            Image(systemName: "chevron.right")
                                                .foregroundColor(.gray)
                                        }
                                        .padding()
                                        .background(Color.white.opacity(0.1))
                                        .cornerRadius(8)
                                    }
                                }
                            }
                            
                            // Similar items
                            if !details.similarItems.isEmpty {
                                Text("You May Also Like")
                                    .font(.title2)
                                    .bold()
                                    .foregroundColor(.white)
                                    .padding(.top, 8)
                                
                                ScrollView(.horizontal, showsIndicators: false) {
                                    HStack(spacing: 12) {
                                        ForEach(details.similarItems) { item in
                                            NavigationLink(destination: DetailsView(itemId: item.id)) {
                                                VStack {
                                                    AsyncImage(url: URL(string: item.imageUrl)) { img in
                                                        img.resizable().aspectRatio(contentMode: .fill)
                                                    } placeholder: {
                                                        Color.gray
                                                    }
                                                    .frame(width: 100, height: 150)
                                                    .cornerRadius(8)
                                                    Text(item.title)
                                                        .font(.caption)
                                                        .foregroundColor(.white)
                                                        .frame(width: 100)
                                                        .lineLimit(1)
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                        .padding(.horizontal)
                    }
                }
            }
        }
        .navigationBarTitleDisplayMode(.inline)
        .onAppear {
            scraper.fetchDetails(id: itemId) { media in
                details = media
                isLoading = false
            }
        }
    }
    
    private func getMovieUrl(for quality: VideoQuality) -> String? {
        switch quality {
        case .p360: return details?.movieUrl360
        case .p720: return details?.movieUrl
        case .p1080: return details?.movieUrl1080
        case .p4K: return details?.movieUrl4k
        }
    }
    
    private func getQualityMap() -> [VideoQuality: String] {
        var map: [VideoQuality: String] = [:]
        if let url360 = details?.movieUrl360, !url360.isEmpty { map[.p360] = url360 }
        if let url720 = details?.movieUrl, !url720.isEmpty { map[.p720] = url720 }
        if let url1080 = details?.movieUrl1080, !url1080.isEmpty { map[.p1080] = url1080 }
        if let url4k = details?.movieUrl4k, !url4k.isEmpty { map[.p4K] = url4k }
        return map
    }
}
"""

with open("UTan/UTan/DetailsView.swift", "w", encoding="utf-8") as f:
    f.write(details_swift)

# 14. Write DownloadsView.swift
downloads_swift = """import SwiftUI

struct DownloadsView: View {
    @ObservedObject var downloadManager = DownloadManager.shared
    @State private var downloadedVideos: [(id: String, title: String, imageUrl: String)] = []
    
    var body: some View {
        NavigationView {
            ZStack {
                Color.black.ignoresSafeArea()
                if downloadedVideos.isEmpty {
                    Text("No downloads yet")
                        .foregroundColor(.gray)
                } else {
                    List {
                        ForEach(downloadedVideos, id: \\.id) { video in
                            NavigationLink(destination: LocalPlayerView(videoId: video.id, title: video.title, imageUrl: video.imageUrl)) {
                                HStack {
                                    AsyncImage(url: URL(string: video.imageUrl)) { img in
                                        img.resizable().aspectRatio(contentMode: .fill)
                                    } placeholder: {
                                        Color.gray
                                    }
                                    .frame(width: 60, height: 90)
                                    .cornerRadius(6)
                                    
                                    Text(video.title)
                                        .foregroundColor(.white)
                                        .font(.headline)
                                }
                            }
                        }
                        .onDelete(perform: deleteDownloads)
                    }
                    .listStyle(PlainListStyle())
                }
            }
            .navigationTitle("Downloads")
        }
        .onAppear {
            refreshDownloadedList()
        }
    }
    
    private func refreshDownloadedList() {
        let fileManager = FileManager.default
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
        do {
            let files = try fileManager.contentsOfDirectory(at: documentsURL, includingPropertiesForKeys: nil)
            var newList: [(id: String, title: String, imageUrl: String)] = []
            for file in files where file.pathExtension == "mp4" {
                let id = file.deletingPathExtension().lastPathComponent
                // We need title and imageUrl - could be stored separately or inferred
                // For now, use id as title placeholder
                newList.append((id: id, title: id, imageUrl: ""))
            }
            downloadedVideos = newList
        } catch {
            print("Failed to list downloads: \\(error)")
        }
    }
    
    private func deleteDownloads(at offsets: IndexSet) {
        for index in offsets {
            let video = downloadedVideos[index]
            let fileManager = FileManager.default
            let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
            let fileURL = documentsURL.appendingPathComponent(video.id).appendingPathExtension("mp4")
            try? fileManager.removeItem(at: fileURL)
        }
        refreshDownloadedList()
    }
}

struct LocalPlayerView: View {
    let videoId: String
    let title: String
    let imageUrl: String
    @State private var player: AVPlayer?
    
    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            if let player = player {
                VideoPlayerRepresentable(player: player, gravity: .resizeAspect)
                    .ignoresSafeArea()
                    .onAppear {
                        player.play()
                    }
                    .onDisappear {
                        player.pause()
                    }
            }
        }
        .navigationTitle(title)
        .navigationBarTitleDisplayMode(.inline)
        .onAppear {
            if let localURL = DownloadManager.shared.getLocalURL(for: videoId) {
                player = AVPlayer(url: localURL)
            }
        }
    }
}
"""

with open("UTan/UTan/DownloadsView.swift", "w", encoding="utf-8") as f:
    f.write(downloads_swift)

# 15. Write ProfileView.swift
profile_swift = """import SwiftUI

struct ProfileView: View {
    @State private var cacheSize: String = "Calculating..."
    
    var body: some View {
        NavigationView {
            List {
                Section {
                    HStack {
                        Image(systemName: "person.circle.fill")
                            .font(.largeTitle)
                        VStack(alignment: .leading) {
                            Text("Guest User")
                                .font(.headline)
                            Text("Not signed in")
                                .font(.caption)
                        }
                    }
                }
                
                Section("Settings") {
                    HStack {
                        Text("Cache Size")
                        Spacer()
                        Text(cacheSize)
                            .foregroundColor(.gray)
                    }
                    Button("Clear Cache") {
                        clearCache()
                    }
                    .foregroundColor(.red)
                }
                
                Section("About") {
                    HStack {
                        Text("Version")
                        Spacer()
                        Text("1.0")
                    }
                }
            }
            .navigationTitle("Profile")
        }
        .onAppear {
            calculateCacheSize()
        }
    }
    
    private func calculateCacheSize() {
        let fileManager = FileManager.default
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
        var totalSize: Int64 = 0
        if let enumerator = fileManager.enumerator(at: documentsURL, includingPropertiesForKeys: [.fileSizeKey]) {
            for case let fileURL as URL in enumerator {
                let attributes = try? fileManager.attributesOfItem(atPath: fileURL.path)
                if let size = attributes?[.size] as? Int64 {
                    totalSize += size
                }
            }
        }
        let formatter = ByteCountFormatter()
        cacheSize = formatter.string(fromByteCount: totalSize)
    }
    
    private func clearCache() {
        let fileManager = FileManager.default
        let documentsURL = fileManager.urls(for: .documentDirectory, in: .userDomainMask).first!
        do {
            let files = try fileManager.contentsOfDirectory(at: documentsURL, includingPropertiesForKeys: nil)
            for file in files where file.pathExtension == "mp4" {
                try fileManager.removeItem(at: file)
            }
            calculateCacheSize()
        } catch {
            print("Failed to clear cache: \\(error)")
        }
    }
}
"""

with open("UTan/UTan/ProfileView.swift", "w", encoding="utf-8") as f:
    f.write(profile_swift)

# 16. Write MainTabView.swift
main_tab_swift = """import SwiftUI

struct MainTabView: View {
    var body: some View {
        TabView {
            HomeView()
                .tabItem {
                    Label("Home", systemImage: "house.fill")
                }
            DownloadsView()
                .tabItem {
                    Label("Downloads", systemImage: "arrow.down.circle.fill")
                }
            ProfileView()
                .tabItem {
                    Label("Profile", systemImage: "person.fill")
                }
        }
        .accentColor(.red)
    }
}
"""

with open("UTan/UTan/MainTabView.swift", "w", encoding="utf-8") as f:
    f.write(main_tab_swift)

print("✅ Project UTan PREMIUM تم إنشاؤه بالكامل مع جميع الإضافات المطلوبة (مشغل متقدم، تحميل، متابعة، ترجمة، جودة، تبويب سفلي، تحسينات عديدة).")
