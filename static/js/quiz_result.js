function createFirework(x, y) {
    const colors = ["#ff0000", "#00ff00", "#0000ff", "#ffff00", "#ff00ff", "#00ffff"];
    for (let i = 0; i < 20; i++) {
      const firework = document.createElement("div");
      firework.className = "firework";
      firework.style.background = colors[Math.floor(Math.random() * colors.length)];
      firework.style.left = `${x}px`;
      firework.style.top = `${y}px`;
      firework.style.transform = `scale(${Math.random() + 0.5})`;
      document.body.appendChild(firework);

      setTimeout(() => firework.remove(), 1000);
    }
  }

  function launchFireworks() {
    const height = window.innerHeight;
    const leftX = 100;
    const rightX = window.innerWidth - 100;

    setInterval(() => createFirework(leftX, Math.random() * height), 800);
    setInterval(() => createFirework(rightX, Math.random() * height), 800);
  }