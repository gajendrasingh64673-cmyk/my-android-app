
# यहाँ अपना Pydroid वाला पूरा PDF Scanner कोड पेस्ट करें
import kivy
from kivy.app import App
# ... (आपका बाकी सारा कोड यहाँ आएगा)
name: Build APK
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Buildozer Action
        uses: ArtemSerebriakov/buildozer-action@v1
        with:
          command: buildozer android debug
