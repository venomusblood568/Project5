document.addEventListener('DOMContentLoaded', function() {
    const randomItemDisplay = document.getElementById('GitaVerses');
    const bhagavadGitaChapters = [
            { chapter: "Arjuna Vishada Yoga", keyVerse: "1.30 - I am unable to stand here any longer, my mind is spinning around, and I see adverse omens, O Keshava." },
            { chapter: "Sankhya Yoga", keyVerse: "2.47 - You have the right to work, but never to the fruit of work. You should never engage in action for the sake of reward, nor should you long for inaction." },
            { chapter: "Karma Yoga", keyVerse: "3.8 - Perform your prescribed duties, for action is better than inaction. A man cannot even maintain his physical body without work." },
            { chapter: "Jnana Karma Sannyasa Yoga", keyVerse: "4.7 - Whenever there is a decline in righteousness and an increase in unrighteousness, at that time I manifest myself on earth." },
            { chapter: "Karma Sannyasa Yoga", keyVerse: "5.3 - A person who neither hates nor desires the fruits of his activities is known to be always renounced." },
            { chapter: "Dhyana Yoga", keyVerse: "6.6 - For him who has conquered the mind, the mind is the best of friends; but for one who has failed to do so, his mind will remain the greatest enemy." },
            { chapter: "Jnana Vijnana Yoga", keyVerse: "7.10 - Of this universe, I am the father; the mother; the support and the grandsire. I am the object of knowledge, the purifier, and the syllable Om." },
            { chapter: "Akshara Parabrahman Yoga", keyVerse: "8.5 - And whoever, at the end of his life, quits his body, remembering Me alone, at once attains My nature." },
            { chapter: "Raja Vidya Raja Guhya Yoga", keyVerse: "9.23 - Those who are devotees of other gods and who worship them with faith actually worship only Me, O son of Kunti, but they do so in a wrong way." },
            { chapter: "Vibhooti Yoga", keyVerse: "10.21 - Of the Adityas I am Vishnu, of lights I am the radiant sun, of the Maruts I am Marici, and among the stars I am the moon." },
            { chapter: "Viswarupa Darshana Yoga", keyVerse: "11.32 - Now I am become Death, the destroyer of worlds." },
            { chapter: "Bhakti Yoga", keyVerse: "12.13 - He who hates no creature, who is friendly and compassionate, who has no possessiveness, who is free from egoism and selfishness..." },
            { chapter: "Kshetra Kshetrajna Vibhaaga Yoga", keyVerse: "13.2 - This body, O son of Kunti, is called the field, and he who knows this body is called the knower of the field." },
            { chapter: "Gunatraya Vibhaga Yoga", keyVerse: "14.11 - When Sattva predominates, O Arjuna, the light of knowledge shines through all the gates of the body." },
            { chapter: "Purushottama Yoga", keyVerse: "15.19 - The Supreme Divine Personality is the ultimate goal of the living entities and the ultimate support." },
            { chapter: "Daivasura Sampad Vibhaga Yoga", keyVerse: "16.2 - Fearlessness, purity of heart, self-restraint, nonviolence, truthfulness, compassion for all beings—these are the divine qualities." },
            { chapter: "Sraddhatraya Vibhaga Yoga", keyVerse: "17.3 - O son of Pritha, the faith of all humans conforms to their nature. The person is of the nature of his faith; as a person’s faith is, so is he." },
            { chapter: "Moksha Sannyasa Yoga", keyVerse: "18.20 - Abandoning all attachment to the results of his activities, ever satisfied and independent, he performs no fruitive action, although engaged in all kinds of undertakings." }
          ];  
    // Function to update the displayed random item
    function updateRandomItem() {
      const randomIndex = Math.floor(Math.random() * bhagavadGitaChapters.length);
      const GitaVerses = bhagavadGitaChapters[randomIndex];
      randomItemDisplay.textContent = `${GitaVerses.chapter}: ${GitaVerses.keyVerse}`;
    }
  
    // Update the random item on page load and every few seconds
    updateRandomItem();
  });
  