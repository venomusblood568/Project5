import UIKit

class ViewController: UIViewController {

    private let imageView: UIImageView = {
        //call of the image
        let imageView = UIImageView()
        //decide the aspect ratio to fill
        imageView.contentMode = .scaleAspectFill
        
        imageView.backgroundColor = .clear
        
        return imageView
    }()
    
    //button parts size, color, outline text
    private let button: UIButton = {
        let button = UIButton()
        button.backgroundColor = .white // Set a background color for visibility
        button.setTitle("New Pic", for: .normal)
        button.setTitleColor(.black, for: .normal)
        button.layer.borderWidth = 1.0 // Add a border
        button.layer.borderColor = UIColor.black.cgColor
        return button
    }()
    //fucntion where it is decided that with each new click you get new picture it will be decide here only
    override func viewDidLoad() {
        super.viewDidLoad()

        view.addSubview(imageView)
        //frame size
        imageView.frame = CGRect(x: 0, y: 0, width: 300, height: 300)
        // position of the frame
        imageView.center = view.center

        view.addSubview(button)

        getRandomPhoto()

        button.addTarget(self, action: #selector(didTapButton), for: .touchUpInside)

        setGradientBackground()
    }
    //position of the button
    override func viewDidLayoutSubviews() {
        super.viewDidLayoutSubviews()
        button.frame = CGRect(x: 50,
                              y: view.frame.size.height - 100 - view.safeAreaInsets.bottom,
                              width: view.frame.size.width - 100,
                              height: 55)
        // Make sure the button stays on top by bringing it to the front
        view.bringSubviewToFront(button)
    }
    //linking of the button
    @objc func didTapButton() {
        getRandomPhoto()
        
    }
    
    //creating a list of gradient to choose from
    func setGradientBackground() {
        let gradientLayer = CAGradientLayer()
        gradientLayer.frame = view.bounds

        // List of 10 different two-color gradients
        let gradients: [[CGColor]] = [
            [UIColor.systemPink.cgColor, UIColor.systemPurple.cgColor],
            [UIColor.systemBlue.cgColor, UIColor.systemTeal.cgColor],
            [UIColor.systemGreen.cgColor, UIColor.systemYellow.cgColor],
            [UIColor.systemOrange.cgColor, UIColor.systemRed.cgColor],
            [UIColor.systemIndigo.cgColor, UIColor.systemGray.cgColor],
            [UIColor.systemRed.cgColor, UIColor.systemPink.cgColor],
            [UIColor.systemTeal.cgColor, UIColor.systemGreen.cgColor],
            [UIColor.systemYellow.cgColor, UIColor.systemOrange.cgColor],
            [UIColor.systemGray.cgColor, UIColor.systemBlue.cgColor],
            [UIColor.systemPurple.cgColor, UIColor.systemIndigo.cgColor]
        ]

        // Choose a random gradient
        let randomGradient = gradients.randomElement() ?? []

        // Set gradient colors using NSArray to avoid type issues
        gradientLayer.colors = NSArray(array: randomGradient) as? [Any]

        view.layer.insertSublayer(gradientLayer, at: 0)
    }
    //fetching of new picture each time
    func getRandomPhoto() {
        let urlString = "https://source.unsplash.com/random/600x600"
        let url = URL(string: urlString)!
        guard let data = try? Data(contentsOf: url) else {
            return
        }
        imageView.image = UIImage(data: data)
    }
}

