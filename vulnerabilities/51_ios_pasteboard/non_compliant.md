
Not in compliance with OWASP Mobile Top 10 for M8 - Side Channel Data
Leakage A general Pasteboard implementation looks like the following

    // setup: let's put some stuff in the UIPasteboard

    let pasteboard = UIPasteboard.general()
    pasteboard.string = "andy"
    pasteboard.url = URL(string: "http://cleanswifter.com")
    pasteboard.image = UIImage()
    pasteboard.color = UIColor.red()

    // understanding the UIPasteboard contents

    if pasteboard.hasStrings {
        print("The pasteboard has Strings!")
    }
    if pasteboard.hasURLs {
        print("The pasteboard has URLs!")
    }
    if pasteboard.hasImages {
        print("The pasteboard has images!")
    }
    if pasteboard.hasColors {
        print("The pasteboard has colors!")
    }

