import SwiftUI
import WebKit

#if os(iOS) || os(visionOS)
struct WebView: UIViewRepresentable {
    let url: URL

    func makeUIView(context: Context) -> WKWebView {
        let webView = WKWebView()
        webView.allowsBackForwardNavigationGestures = true
        return webView
    }

    func updateUIView(_ uiView: WKWebView, context: Context) {
        let request = URLRequest(url: url)
        uiView.load(request)
    }
}
#elseif os(macOS)
struct WebView: NSViewRepresentable {
    let url: URL
    
    func makeNSView(context: Context) -> WKWebView {
        let webView = WKWebView()
        webView.allowsBackForwardNavigationGestures = true
        return webView
    }
    
    func updateNSView(_ nsView: WKWebView, context: Context) {
        let request = URLRequest(url: url)
        nsView.load(request)
    }
}
#endif

struct ContentView: View {
    private var isPreview: Bool {
        return ProcessInfo.processInfo.environment["XCODE_RUNNING_FOR_PREVIEWS"] == "1"
    }
    
    var body: some View {
        #if DEBUG
        if isPreview {
            // Placeholder only shown in Xcode preview
            VStack {
                Text("Pure")
                    .font(.largeTitle)
                    .padding()
                Text("Web content will load on device")
                    .foregroundColor(.secondary)
            }
        } else {
            // Show actual WebView in simulator and on device
            WebView(url: URL(string: "https://purity21-streak-tracker.lovable.app")!)
                .edgesIgnoringSafeArea(.all)
        }
        #else
        // Always show WebView in Release builds
        WebView(url: URL(string: "https://purity21-streak-tracker.lovable.app")!)
            .edgesIgnoringSafeArea(.all)
        #endif
    }
}

#Preview {
    ContentView()
}
