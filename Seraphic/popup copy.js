function updateCountdown() {
    const targetDate = new Date('2026-10-26T00:00:00Z');
    const currentDate = new Date();

    const years = targetDate.getFullYear() - currentDate.getFullYear();
    const targetMonth = targetDate.getMonth();
    const currentMonth = currentDate.getMonth();

    let months = targetMonth - currentMonth;
    if (currentDate > targetDate || (currentDate.getMonth() === targetDate.getMonth() && currentDate.getDate() > targetDate.getDate())) {
        months += 12;
    }

    const days = targetDate.getDate() - currentDate.getDate();
    const hours = targetDate.getHours() - currentDate.getHours();
    const minutes = targetDate.getMinutes() - currentDate.getMinutes();
    const seconds = targetDate.getSeconds() - currentDate.getSeconds();

    if (months <= 0 && days <= 0 && hours <= 0 && minutes <= 0 && seconds <= 0) {
        // If the target date has passed, display a message
        document.getElementById('countdown').textContent = "Today is the day!";
    } else {
        document.getElementById('countdown').textContent = `
            Years: ${years}
            Months: ${months}
            Days: ${days}
            Hours: ${hours}
            Minutes: ${minutes}
            Seconds: ${seconds}
        `;
    }
}

// Update countdown every second
setInterval(updateCountdown, 1000);

// Initial call to display countdown immediately
updateCountdown();
