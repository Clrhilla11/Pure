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
    @Environment(\.previewDevice) private var previewDevice
    
    var body: some View {
        // Check if we're in preview mode to avoid network requests during preview
        if ProcessInfo.processInfo.environment["XCODE_RUNNING_FOR_PREVIEWS"] == "1" {
            // Placeholder content for preview
            VStack {
                Text("Pure")
                    .font(.largeTitle)
                    .padding()
                Text("Web content will load on device")
                    .foregroundColor(.secondary)
            }
        } else {
            // Real WebView for actual runtime
            WebView(url: URL(string: "https://purity21-streak-tracker.lovable.app")!)
                .edgesIgnoringSafeArea(.all)
        }
    }
}

#Preview {
    ContentView()
}
