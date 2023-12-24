//
//  ContentView.swift
//  login_page
//
//  Created by Gourav Anand Jha on 02/10/1945 Saka.
//

import SwiftUI

struct ContentView: View {
    
    @State private var username = ""
    @State private var password = ""
    @State private var wrongUsername : Float = 0
    @State private var wrongPassword : Float = 0
    @State private var showingLoginScreen = false
    
    var body: some View {
        NavigationView {
            ZStack {
                // Background styling
                Color.blue.ignoresSafeArea()
                Circle().scale(1.7).foregroundColor(.white.opacity(0.15))
                Circle().scale(1.35).foregroundColor(.white)
                
                VStack {
                    Text("Login")
                        .font(.largeTitle)
                        .bold()
                        .padding()
                        .foregroundColor(.black)
                    
                    TextField("Username", text: $username)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.5))
                        .cornerRadius(10)
                        .border(.red,width:CGFloat(wrongUsername))
                    
                    SecureField("Password", text: $password)
                        .padding()
                        .frame(width: 300, height: 50)
                        .background(Color.black.opacity(0.5))
                        .cornerRadius(10)
                        .border(.red,width:CGFloat(wrongPassword))
                    
                    Button("Login"){
                        authenticateUser(username: username, password: password)
                    }
                    .foregroundColor(.white)
                    .frame(width: 300,height: 50)
                    .background(Color.blue)
                    .cornerRadius(10)
                    
                    NavigationLink(destination: Text("You are logged in @\(username)"), isActive: $showingLoginScreen) {
                        EmptyView()
                    }
                }
                

                }
        }
        .navigationBarHidden(true) // Hide the navigation bar
    }
    func authenticateUser(username: String, password: String) {
            if username.lowercased() == "sam2021" {
                wrongUsername = 0
                if password.lowercased() == "abc123" {
                    wrongPassword = 0
                    showingLoginScreen = true
                } else {
                    wrongPassword = 2
                }
            } else {
                wrongUsername = 2
            }
        }
}

// Preview for testing in Xcode
struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
