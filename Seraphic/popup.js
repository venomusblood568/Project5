function updateCountdown() {
    const targetDate = new Date('2026-10-26T00:00:00Z'); // October 26, 2026, 12:00 AM (midnight)
    const currentDate = new Date();

    const years = targetDate.getFullYear() - currentDate.getFullYear();
    const targetMonth = targetDate.getMonth();
    const currentMonth = currentDate.getMonth();

    let months = targetMonth - currentMonth;
    if (currentDate.getDate() > targetDate.getDate()) {
        months--;
    }

    if (months < 0) {
        months += 12;
    }

    const daysInTargetMonth = new Date(currentDate.getFullYear(), currentMonth + 1, 0).getDate();
    let days = daysInTargetMonth - currentDate.getDate() + targetDate.getDate();
    if (currentDate.getDate() > targetDate.getDate()) {
        months--;
        days = daysInTargetMonth - currentDate.getDate() + 1;
    }

    let hours = targetDate.getHours() - currentDate.getHours();
    let minutes = targetDate.getMinutes() - currentDate.getMinutes();
    let seconds = targetDate.getSeconds() - currentDate.getSeconds();

    if (seconds < 0) {
        seconds += 60;
        minutes--;
    }

    if (minutes < 0) {
        minutes += 60;
        hours--;
    }

    if (hours < 0) {
        hours += 24;
        days--;
    }

    document.getElementById('countdown').textContent = `${years} years, ${months} months, ${days} days, ${hours} hours, ${minutes} minutes, and ${seconds} seconds left until the big day!`;
}

// Update countdown every second
setInterval(updateCountdown, 1000);

// Initial call to display countdown immediately
updateCountdown();
