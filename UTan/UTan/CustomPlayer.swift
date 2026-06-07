import SwiftUI
import AVKit
import AVFoundation

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
    
    @Environment(\.presentationMode) var presentation
    @StateObject private var progressStore = WatchProgressStore.shared
    @StateObject private var settings = AppSettings.shared
    
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
    
    @State private var playbackSpeed: Double = 1.0
    @State private var saveTimer: Timer?
    @State private var errorMessage: String?
    
    private var subtitleFont: Font {
        if let customFont = UIFont(name: "Cairo", size: CGFloat(settings.subtitleFontSize)) {
            return Font(customFont)
        } else {
            return .system(size: CGFloat(settings.subtitleFontSize), weight: .bold, design: .rounded)
        }
    }
    
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
                        .padding(.horizontal, 16)
                        .padding(.vertical, 8)
                        .background(Color.red.opacity(0.85))
                        .cornerRadius(20)
                        .padding(.top, 60)
                        Spacer()
                    }
                }
                
                if settings.subtitlesEnabled && !activeSub.isEmpty {
                    VStack {
                        Spacer()
                        Text(activeSub)
                            .font(subtitleFont)
                            .foregroundColor(settings.subtitleColor)
                            .shadow(color: .black, radius: 3, x: 1, y: 1)
                            .multilineTextAlignment(.center)
                            .padding(.horizontal, 20)
                            .padding(.vertical, 6)
                            .background(Color.black.opacity(settings.subtitleBgOpacity))
                            .cornerRadius(8)
                            .padding(.bottom, CGFloat(settings.subtitleBottomPad))
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
                    Text("جاري التحميل...")
                        .foregroundColor(.white)
                    Button("إغلاق") {
                        presentation.wrappedValue.dismiss()
                    }
                    .padding()
                    .background(UT_RED)
                    .foregroundColor(.white)
                    .cornerRadius(8)
                }
            }
        }
        .statusBar(hidden: true)
        .onAppear { setupPlayer() }
        .onDisappear { shutdown() }
    }
    
    @ViewBuilder
    private func controlsOverlay(player: AVPlayer) -> some View {
        VStack {
            HStack {
                if !isLocked {
                    Button { shutdown(); presentation.wrappedValue.dismiss() } label: {
                        Image(systemName: "arrow.backward")
                            .playerBtn()
                    }
                    Spacer()
                    VStack(spacing: 2) {
                        Text(episodeTitle.isEmpty ? itemTitle : episodeTitle)
                            .font(.system(size: 14, weight: .bold))
                            .foregroundColor(.white)
                            .lineLimit(1)
                        Image("logo") // logo.png from Assets
                            .resizable()
                            .scaledToFit()
                            .frame(height: 12)
                            .opacity(0.8)
                    }
                    Spacer()
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
            .padding(.horizontal, 16)
            .padding(.top, 20)
            .background(
                LinearGradient(colors: [.black.opacity(0.8), .clear],
                               startPoint: .top, endPoint: .bottom)
            )
            
            Spacer()
            
            if !isLocked {
                VStack(spacing: 12) {
                    HStack(spacing: 10) {
                        Text(formatTime(isDragging ? seekTarget : currentTime))
                            .timeLabel()
                        Slider(
                            value: isDragging ? $seekTarget : $currentTime,
                            in: 0...max(duration, 1)
                        ) { editing in
                            isDragging = editing
                            if !editing {
                                player.seek(to: CMTime(seconds: seekTarget, preferredTimescale: 600))
                                currentTime = seekTarget
                                scheduleHide()
                            }
                        }
                        .accentColor(UT_RED)
                        Text(formatTime(duration))
                            .timeLabel()
                    }
                    .padding(.horizontal, 16)
                    
                    HStack(spacing: 50) {
                        Button {
                            let t = max(0, currentTime - 10)
                            player.seek(to: CMTime(seconds: t, preferredTimescale: 600))
                            scheduleHide()
                        } label: {
                            Image(systemName: "gobackward.10").font(.title).foregroundColor(.white)
                        }
                        
                        Button {
                            if isPlaying { player.pause() }
                            else { player.rate = Float(playbackSpeed) }
                            isPlaying.toggle()
                            scheduleHide()
                        } label: {
                            Image(systemName: isPlaying ? "pause.circle.fill" : "play.circle.fill")
                                .font(.system(size: 66))
                                .foregroundColor(UT_RED)
                                .background(Circle().fill(Color.white))
                        }
                        
                        Button {
                            let t = min(duration, currentTime + 10)
                            player.seek(to: CMTime(seconds: t, preferredTimescale: 600))
                            scheduleHide()
                        } label: {
                            Image(systemName: "goforward.10").font(.title).foregroundColor(.white)
                        }
                    }
                    
                    HStack(spacing: 6) {
                        ForEach(VideoQuality.allCases) { q in
                            Button(q.rawValue) { switchQuality(to: q) }
                                .font(.system(size: 12, weight: quality == q ? .bold : .regular))
                                .foregroundColor(quality == q ? .white : .white.opacity(0.6))
                                .padding(.horizontal, 10).padding(.vertical, 6)
                                .background(quality == q ? UT_RED : Color.clear)
                                .cornerRadius(8)
                        }
                        Spacer()
                        Button {
                            let all = VideoFitMode.allCases
                            let idx = all.firstIndex(of: fitMode) ?? 0
                            fitMode = all[(idx + 1) % all.count]
                        } label: {
                            Image(systemName: "aspectratio")
                                .font(.caption).foregroundColor(.white.opacity(0.8))
                        }
                        Text(fitMode.rawValue)
                            .font(.system(size: 11))
                            .foregroundColor(.white.opacity(0.7))
                    }
                    .padding(.horizontal, 16)
                    .padding(.bottom, 20)
                }
                .background(
                    LinearGradient(colors: [.clear, .black.opacity(0.9)],
                                   startPoint: .top, endPoint: .bottom)
                )
            }
        }
    }
    
    private func setupPlayer() {
        let resumeTime = progressStore.progress(for: itemId)?.progressSeconds ?? 0
        let urlStr = resolvedUrl(quality: quality)
        
        guard !urlStr.isEmpty, let url = URL(string: urlStr) else {
            errorMessage = "رابط الفيديو غير صالح"
            return
        }
        
        let item = AVPlayerItem(url: url)
        let p = AVPlayer(playerItem: item)
        self.player = p
        
        if resumeTime > 5 {
            p.seek(to: CMTime(seconds: resumeTime, preferredTimescale: 600))
        }
        p.play()
        
        NotificationCenter.default.addObserver(
            forName: .AVPlayerItemDidPlayToEndTime,
            object: item, queue: .main) { _ in self.isPlaying = false }
        
        Task {
            if let dur = try? await item.asset.load(.duration) {
                DispatchQueue.main.async { self.duration = dur.seconds }
            }
        }
        
        timeObserver = p.addPeriodicTimeObserver(
            forInterval: CMTime(seconds: 0.25, preferredTimescale: 600), queue: .main
        ) { t in
            if !self.isDragging { self.currentTime = t.seconds }
            if let cue = self.cues.first(where: { t.seconds >= $0.startTime && t.seconds <= $0.endTime }) {
                self.activeSub = cue.text
            } else {
                self.activeSub = ""
            }
        }
        
        let subUrl = subtitleVttUrl.isEmpty ? subtitleUrl : subtitleVttUrl
        if !subUrl.isEmpty {
            SubtitleParser.parse(url: subUrl) { parsedCues in
                self.cues = parsedCues
            }
        }
        
        scheduleHide()
        saveTimer = Timer.scheduledTimer(withTimeInterval: 5, repeats: true) { _ in
            guard let p = self.player, self.duration > 0 else { return }
            progressStore.save(
                itemId: self.itemId,
                title: self.itemTitle,
                imageUrl: self.itemImageUrl,
                episodeId: self.episodeId,
                episodeTitle: self.episodeTitle,
                progress: p.currentTime().seconds,
                duration: self.duration,
                videoUrl: self.videoUrl,
                videoUrl1080: self.videoUrl1080,
                videoUrl360: self.videoUrl360,
                subUrl: self.subtitleUrl,
                subVttUrl: self.subtitleVttUrl
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
            withAnimation { self.showControls = false }
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
        case .q360:  return fixUrl(videoUrl360.isEmpty ? videoUrl : videoUrl360)
        case .q1080: return fixUrl(videoUrl1080.isEmpty ? videoUrl : videoUrl1080)
        default:     return fixUrl(videoUrl)
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
        self.font(.title3)
            .foregroundColor(color)
            .padding(12)
            .background(Color.white.opacity(0.15))
            .clipShape(Circle())
    }
}
extension Text {
    func timeLabel() -> some View {
        self.font(.system(size: 12, weight: .semibold)).monospacedDigit().foregroundColor(.white)
    }
}
