document.addEventListener('DOMContentLoaded', function() {
    const randomItemDisplay = document.getElementById('HeavenlyScript');
    const HeavenlyScriptChapters = [
            { chapter: "Genesis 1:1", keyVerse: "In the beginning, God created the heavens and the earth." },
            { chapter: "Exodus 20:13", keyVerse: "You shall not murder."},
            { chapter: "Psalm 23:1", keyVerse: "The Lord is my shepherd; I shall not want."},
            { chapter: "Proverbs 3:5-6", keyVerse: "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways acknowledge Him, and He shall direct your paths."},
            { chapter: "Isaiah 53:5", keyVerse: "But he was wounded for our transgressions, he was bruised for our iniquities: the chastisement of our peace was upon him; and with his stripes, we are healed."},
            { chapter: "Matthew 5:3-12", keyVerse: "The Beatitudes, describing blessings for the poor in spirit, those who mourn, the meek, those who hunger and thirst for righteousness, the merciful, the pure in heart, the peacemakers, and those persecuted for righteousness' sake."},
            { chapter: "John 3:16", keyVerse: "For God so loved the world that he gave his only begotten Son, that whoever believes in Him should not perish but have everlasting life."},
            { chapter: "Romans 8:28", keyVerse: "And we know that all things work together for good to those who love God, to those who are the called according to His purpose."},
            { chapter: "1 Corinthians 13:4-7", keyVerse: "The famous description of love: Love is patient, love is kind. It does not envy, it does not boast, it is not proud..."},
            { chapter: "Revelation 21:4", keyVerse: "And God shall wipe away all tears from their eyes; and there shall be no more death, neither sorrow, nor crying, neither shall there be any more pain: for the former things are passed away."},
          ];  
    // Function to update the displayed random item
    function updateRandomItem() {
      const randomIndex = Math.floor(Math.random() * HeavenlyScriptChapters.length);
      const HeavenlyScript = HeavenlyScriptChapters[randomIndex];
      randomItemDisplay.textContent = `${HeavenlyScript.chapter}: ${HeavenlyScript.keyVerse}`;
    }
  
    // Update the random item on page load and every few seconds
    updateRandomItem();
  });
  