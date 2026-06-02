
const navStyles = `
    .nav-floating {
        position: fixed;
        bottom: 2rem;
        left: 50%;
        transform: translateX(-50%);
        background: rgba(10, 15, 20, 0.85);
        backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 9999px;
        padding: 0.75rem 2rem;
        z-index: 9999;
        display: flex;
        gap: 2rem;
        box-shadow: 0 10px 30px -5px rgba(0, 0, 0, 0.5);
        transition: all 0.3s ease;
    }

    .nav-floating:hover {
        border-color: rgba(0, 243, 255, 0.3);
        box-shadow: 0 0 20px rgba(0, 243, 255, 0.15);
    }

    .nav-item {
        color: #9ca3af;
        text-decoration: none;
        display: flex;
        flex-direction: column;
        align-items: center;
        gap: 0.25rem;
        transition: all 0.2s;
        font-family: 'Space Grotesk', sans-serif;
    }

    .nav-item:hover, .nav-item.active {
        color: #00f3ff;
        transform: translateY(-2px);
    }

    .nav-item i {
        font-size: 1.25rem;
    }

    .nav-item span {
        font-size: 0.65rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        font-weight: 600;
    }
`;

const navHtml = `
<nav class="nav-floating">
    <a href="dashboard.html" class="nav-item" id="nav-dashboard">
        <i class="fa-solid fa-chart-pie"></i>
        <span>Dashboard</span>
    </a>
    <a href="index.html" class="nav-item" id="nav-index">
        <i class="fa-solid fa-book-open"></i>
        <span>Library</span>
    </a>
    <a href="quiz.html" class="nav-item" id="nav-quiz">
        <i class="fa-solid fa-gamepad"></i>
        <span>Quiz</span>
    </a>
    <a href="semantic_search.html" class="nav-item" id="nav-search">
        <i class="fa-solid fa-brain"></i>
        <span>AI Search</span>
    </a>
</nav>
`;

// Inject Styles
const styleSheet = document.createElement("style");
styleSheet.innerText = navStyles;
document.head.appendChild(styleSheet);

// Inject HTML
document.body.insertAdjacentHTML('beforeend', navHtml);

// Highlight Active Link
const currentPage = window.location.pathname.split('/').pop() || 'index.html';
const activeId = 'nav-' + currentPage.replace('.html', '');
const activeEl = document.getElementById(activeId);
if (activeEl) activeEl.classList.add('active');
