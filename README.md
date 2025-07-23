# Steam AppID Display

A Millennium plugin that displays the AppID of games underneath their titles on Steam store pages, complete with a handy copy button.

## Features

- Displays the AppID under game titles on Steam store pages
- One-click copy button to copy the AppID to your clipboard
- Clean, Steam-native UI that matches the store's design
- Lightweight and non-intrusive
- Built with webkit.js for better compatibility with Millennium
- Works with both traditional and React-based Steam store pages

## Installation

1. Ensure you have [Millennium](https://github.com/SteamClientHomebrew/Millennium) installed
2. Clone this repository to your Millennium plugins folder:
   ```
   git clone https://github.com/yourusername/steam-appid-display "%PROGRAMFILES(X86)%\Steam\plugins\steam-appid-display"
   ```
3. Restart Steam or reload Millennium
4. The plugin should now be active - visit any Steam store page to see it in action!

## Usage

1. Navigate to any Steam store page (e.g., `store.steampowered.com/app/730` for CS2)
2. Look for the AppID displayed under the game's title
3. Click the copy button to copy the AppID to your clipboard

## Building from Source

1. Clone this repository
2. Install dependencies:
   ```
   pnpm install
   ```
3. Build the plugin:
   ```
   pnpm run build
   ```
4. The built plugin will be in the `dist` folder

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT
