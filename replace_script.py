import re

with open('hackexpo.html', 'r') as f:
    content = f.read()

# Replace CSS
css_new = """    /* ── NEW LAYOUT REVEAL ─────────────────────────────────────────────────────── */
    #reveal {
      position: fixed;
      inset: 0;
      z-index: 20;
      opacity: 0;
      pointer-events: none;
      transition: opacity 1s ease 0.3s;
      display: flex;
      flex-direction: column;
      padding: 40px 60px;
    }

    #reveal.visible {
      opacity: 1;
      pointer-events: all;
    }

    .top-nav {
      display: flex;
      justify-content: space-between;
      align-items: center;
      width: 100%;
      border-bottom: 1px solid rgba(255, 255, 255, 0.1);
      padding-bottom: 20px;
    }

    .top-nav .logo {
      font-family: 'Outfit', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: #fff;
      letter-spacing: 2px;
    }

    .nav-btn {
      background: #fff;
      color: #000;
      border: none;
      border-radius: 100px;
      padding: 10px 24px;
      font-family: 'Inter', sans-serif;
      font-weight: 600;
      font-size: 14px;
      cursor: pointer;
      transition: transform 0.3s;
    }
    .nav-btn:hover {
      transform: translateY(-2px);
    }

    .main-layout {
      display: flex;
      flex: 1;
      margin-top: 60px;
    }

    .content-left {
      flex: 1;
      display: flex;
      flex-direction: column;
      justify-content: center;
      max-width: 800px;
      z-index: 2;
    }

    .content-right {
      flex: 1;
      display: flex;
      align-items: center;
      justify-content: center;
      position: relative;
    }

    .top-eyebrow {
      font-family: 'Inter', sans-serif;
      font-size: 12px;
      letter-spacing: 4px;
      color: rgba(255, 255, 255, 0.6);
      text-transform: uppercase;
      margin-bottom: 24px;
      display: flex;
      align-items: center;
    }
    .top-eyebrow::before {
      content: '';
      display: inline-block;
      width: 40px;
      height: 1px;
      background: rgba(255, 255, 255, 0.6);
      margin-right: 15px;
    }

    .huge-title {
      font-family: 'Outfit', sans-serif;
      font-size: clamp(50px, 6vw, 90px);
      font-weight: 800;
      line-height: 1.1;
      color: #fff;
      letter-spacing: -2px;
      margin-bottom: 40px;
      text-transform: uppercase;
    }

    .huge-title .highlight {
      background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
      display: inline-block;
      filter: drop-shadow(0 0 10px rgba(0, 242, 254, 0.4));
    }

    .dates-block {
      background: rgba(0, 242, 254, 0.05);
      border-left: 2px solid #00f2fe;
      padding: 20px 30px;
      margin-bottom: 40px;
      max-width: 600px;
    }

    .event-dates-new {
      font-family: 'Outfit', sans-serif;
      font-size: 24px;
      font-weight: 700;
      color: #fff;
      margin-bottom: 12px;
      letter-spacing: 2px;
    }

    .dates-desc {
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      color: rgba(255, 255, 255, 0.7);
      line-height: 1.6;
    }

    .countdown-strip {
      display: flex;
      gap: 24px;
      margin-bottom: 40px;
    }

    .countdown-unit {
      background: rgba(255, 255, 255, 0.03);
      border: 1px solid rgba(255, 255, 255, 0.1);
      border-radius: 8px;
      padding: 15px 20px;
      text-align: center;
      min-width: 90px;
    }

    .countdown-num {
      font-family: 'Outfit', sans-serif;
      font-size: 32px;
      font-weight: 700;
      color: #00f2fe;
      margin-bottom: 4px;
    }

    .countdown-label {
      font-family: 'Inter', sans-serif;
      font-size: 10px;
      font-weight: 600;
      letter-spacing: 2px;
      color: rgba(255, 255, 255, 0.5);
    }

    .register-btn {
      font-family: 'Inter', sans-serif;
      font-size: 16px;
      font-weight: 700;
      padding: 18px 48px;
      background: #fff;
      color: #000;
      border: none;
      border-radius: 100px;
      cursor: pointer;
      align-self: flex-start;
      transition: all 0.3s ease;
      text-transform: uppercase;
      letter-spacing: 1px;
    }

    .register-btn:hover {
      transform: translateY(-3px);
      box-shadow: 0 10px 30px rgba(255, 255, 255, 0.2);
    }

    /* 3D CUBE SCENE */
    .scene {
      width: 400px;
      height: 400px;
      perspective: 1200px;
    }

    .cube {
      width: 100%;
      height: 100%;
      position: relative;
      transform-style: preserve-3d;
      animation: rotateCube 20s infinite linear;
    }

    @keyframes rotateCube {
      0% { transform: rotateX(0deg) rotateY(0deg); }
      100% { transform: rotateX(360deg) rotateY(360deg); }
    }

    .face {
      position: absolute;
      width: 300px;
      height: 300px;
      top: 50px;
      left: 50px;
      border: 4px solid #00f2fe;
      box-shadow: 0 0 30px rgba(0, 242, 254, 0.4), inset 0 0 30px rgba(0, 242, 254, 0.4);
      background: rgba(0, 242, 254, 0.05);
      backdrop-filter: blur(2px);
    }

    .front  { transform: translateZ(150px); }
    .back   { transform: rotateY(180deg) translateZ(150px); }
    .right  { transform: rotateY(90deg) translateZ(150px); }
    .left   { transform: rotateY(-90deg) translateZ(150px); }
    .top    { transform: rotateX(90deg) translateZ(150px); }
    .bottom { transform: rotateX(-90deg) translateZ(150px); }

    .orb {
      position: absolute;
      width: 150px;
      height: 150px;
      top: 125px;
      left: 125px;
      background: radial-gradient(circle, #4facfe, #00f2fe, transparent);
      border-radius: 50%;
      box-shadow: 0 0 60px 20px rgba(0, 242, 254, 0.6);
      transform: translateZ(0);
      animation: pulseOrb 4s infinite alternate ease-in-out;
    }

    @keyframes pulseOrb {
      0% { transform: scale(0.9); opacity: 0.8; }
      100% { transform: scale(1.1); opacity: 1; }
    }

    /* Small floating orbs in background */
    .bg-glow-mini {
      position: absolute;
      width: 80px;
      height: 80px;
      background: #00f2fe;
      border-radius: 50%;
      filter: blur(40px);
      opacity: 0.6;
    }
    .bg-glow-mini.pos1 { top: 20%; left: 10%; animation: floatMini 8s infinite alternate; }
    .bg-glow-mini.pos2 { bottom: 30%; right: 5%; animation: floatMini 10s infinite alternate-reverse; }

    @keyframes floatMini {
      0% { transform: translateY(0); }
      100% { transform: translateY(-30px); }
    }
  </style>"""

content = re.sub(r'/\* ── REVEAL ─────────────────────────────────────────────────────── \*/.*?</style>', css_new, content, flags=re.DOTALL)


# Replace HTML
html_new = """  <!-- REVEAL -->
  <div id="reveal">
    <nav class="top-nav">
      <div class="logo">HackExpo</div>
      <button class="nav-btn">Register &rarr;</button>
    </nav>
    
    <div class="main-layout">
      <div class="content-left">
        <div class="top-eyebrow">Innovation at every turn</div>
        <div class="huge-title">
          EDUCATIONAL SIMULATION / <br>
          <span class="highlight">HACKEXPO /</span> <br>
          INNOVATION /
        </div>
        
        <div class="dates-block">
          <div class="event-dates-new">ON 29TH & 30TH MAY</div>
          <p class="dates-desc">Join us at HackExpo to learn, compete, and connect with the cybersecurity community through workshops, CTFs, and expert sessions.</p>
        </div>

        <div class="countdown-strip" id="countdown-strip">
          <div class="countdown-unit">
            <div class="countdown-num" id="cd-days">00</div>
            <div class="countdown-label">DAYS</div>
          </div>
          <div class="countdown-unit">
            <div class="countdown-num" id="cd-hrs">00</div>
            <div class="countdown-label">HOURS</div>
          </div>
          <div class="countdown-unit">
            <div class="countdown-num" id="cd-min">00</div>
            <div class="countdown-label">MINUTES</div>
          </div>
          <div class="countdown-unit">
            <div class="countdown-num" id="cd-sec">00</div>
            <div class="countdown-label">SECONDS</div>
          </div>
        </div>
        
        <button class="register-btn">Let's Talk &rarr;</button>
      </div>
      
      <div class="content-right">
        <!-- 3D CSS Cube -->
        <div class="scene">
          <div class="cube">
            <div class="face front"></div>
            <div class="face back"></div>
            <div class="face right"></div>
            <div class="face left"></div>
            <div class="face top"></div>
            <div class="face bottom"></div>
            <div class="orb"></div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="bg-glow-mini pos1"></div>
  <div class="bg-glow-mini pos2"></div>

  <script>"""

content = re.sub(r'<!-- REVEAL -->.*?<script>', html_new, content, flags=re.DOTALL)

with open('hackexpo.html', 'w') as f:
    f.write(content)
print("Done")
