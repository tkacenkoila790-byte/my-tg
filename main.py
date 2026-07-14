import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.utils import executor

API_TOKEN = '8908913545:AAFqVtBWMZNTrJQKGJxDPyi3wsSHC9iv77Y'
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# ==========================================
# 1. БЛОК: ПРИВЕТСТВИЕ И ЗАПУСК (УЖЕ ЕСТЬ)
# ==========================================
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    welcome_text = (
        "Здравствуй мой друг, ты попал в крипто бота основного на компании @send..."
    )
    keyboard = InlineKeyboardMarkup().add(
        InlineKeyboardButton(
            text="🚀 Запустить приложение", 
            web_app=WebAppInfo(url="https://my-tg-01l6.onrender.com")
        )
    )
    await message.reply(welcome_text, reply_markup=keyboard)

# ==========================================
# 2. НОВЫЙ БЛОК: ОБРАБОТКА ДАННЫХ ИЗ WEB APP
# ==========================================
# Сюда будут приходить данные от мини-приложения, 
# например, когда пользователь привязывает телефон в настройках сайта
@dp.message_handler(content_types=['web_app_data'])
async def handle_web_app_data(message: types.Message):
    received_data = message.web_app_data.data
    # Здесь пишется код, который сохраняет телефон в базу данных
    await message.answer(f"Данные успешно обновлены: {received_data}")

# ==========================================
# 3. НОВЫЙ БЛОК: АДМИН-КОМАНДЫ (Управление балансом)
# ==========================================
# Сюда можно добавить команды для вас, чтобы управлять игрой
@dp.message_handler(commands=['admin'])
async def admin_panel(message: types.Message):
    # Проверяем, ваш ли это Telegram ID
    if message.from_user.id == 123456789: # Замените на свой ID
        await message.answer("Добро пожаловать в админ-панель. Здесь можно настраивать балансы.")
    else:
        await message.answer("У вас нет доступа к этой команде.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

:root {
    --bg-color: #0b141c;
    --card-bg: #16222f;
    --accent-blue: #2481cc;
    --text-main: #ffffff;
    --text-muted: #7e8b98;
    --green: #2ecc71;
}

.light-theme {
    --bg-color: #f0f4f8;
    --card-bg: #ffffff;
    --accent-blue: #1a73e8;
    --text-main: #1c1c1c;
    --text-muted: #5f6368;
}

body {
    margin: 0;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    background-color: var(--bg-color);
    color: var(--text-main);
    display: flex;
    flex-direction: column;
    align-items: center;
}

/* Шапка */
.header {
    width: 100%;
    max-width: 450px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 15px;
    box-sizing: border-box;
}

.user-info { display: flex; align-items: center; gap: 10px; }
.avatar { background: var(--accent-blue); width: 35px; height: 35px; border-radius: 50%; display: flex; align-items: center; justify-content: center; }
.settings-btn { background: none; border: none; font-size: 20px; cursor: pointer; }

/* Кошелек */
.wallet-container {
    width: 100%;
    max-width: 450px;
    padding: 10px 15px;
    box-sizing: border-box;
}

.balance-card {
    background: linear-gradient(135deg, #1d3557, var(--accent-blue));
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    margin-bottom: 15px;
}
.balance-label { color: rgba(255,255,255,0.7); font-size: 14px; margin: 0; }
.balance-amount { font-size: 32px; margin: 5px 0 0 0; }

/* Кнопки действий */
.action-buttons {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    margin-bottom: 20px;
}
.action-btn {
    flex: 1;
    background: var(--card-bg);
    border: none;
    color: var(--text-main);
    padding: 12px;
    border-radius: 12px;
    cursor: pointer;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 5px;
    font-size: 13px;
    font-weight: bold;
}

/* Курсы */
.crypto-rates {
    background: var(--card-bg);
    border-radius: 14px;
    padding: 12px;
    margin-bottom: 20px;
}
.rate-item {
    display: flex;
    justify-content: space-between;
    padding: 8px 0;
    border-bottom: 1px solid rgba(255,255,255,0.05);
}
.rate-item:last-child { border: none; }

/* Игра Ракетка */
.crash-game {
    background: var(--card-bg);
    border-radius: 16px;
    padding: 15px;
}
.game-title { font-size: 16px; color: var(--accent-blue); margin-top: 0; }
.game-screen {
    background: #090f16;
    height: 180px;
    border-radius: 12px;
    position: relative;
    overflow: hidden;
    display: flex;
    justify-content: center;
    align-items: center;
}
.multiplier { font-size: 42px; color: var(--green); font-weight: bold; z-index: 2; }
.rocket {
    font-size: 35px;
    position: absolute;
    bottom: 10px;
    left: 10px;
    transition: transform 0.1s linear;
}

/* Элементы управления ставкой */
.bet-controls { display: flex; flex-direction: column; gap: 10px; margin-top: 15px; }
.bet-input {
    background: #090f16;
    border: 1px solid #233549;
    color: white;
    padding: 12px;
    border-radius: 8px;
    text-align: center;
    font-size: 16px;
}
.start-btn {
    background: var(--accent-blue);
    color: white;
    border: none;
    padding: 14px;
    border-radius: 8px;
    font-weight: bold;
    cursor: pointer;
    font-size: 16px;
}

/* Настройки (Модальное окно) */
.modal {
    display: none;
    position: fixed;
    top: 0; left: 0; width: 100%; height: 100%;
    background: rgba(0,0,0,0.6);
    justify-content: center;
    align-items: center;
    z-index: 10;
}
.modal-content {
    background: var(--card-bg);
    padding: 20px;
    border-radius: 16px;
    width: 85%;
    max-width: 350px;
}
.setting-row {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 15px;
}
.setting-row select, .setting-row input {
    background: #090f16;
    border: 1px solid #233549;
    color: white;
    padding: 6px;
    border-radius: 6px;
}
.close-btn { width: 100%; padding: 10px; background: #e74c3c; color: white; border: none; border-radius: 8px; cursor: pointer; }
// Переключение окна настроек
function toggleSettings() {
    const modal = document.getElementById('settingsModal');
    modal.style.display = modal.style.display === 'flex' ? 'none' : 'flex';
}

// Смена темы (Светлая / Темная)
function changeTheme() {
    const theme = document.getElementById('themeSelect').value;
    if (theme === 'light') {
        document.body.classList.remove('dark-theme');
        document.body.classList.add('light-theme');
    } else {
        document.body.classList.remove('light-theme');
        document.body.classList.add('dark-theme');
    }
}

// Заглушка для P2P-маркета
function openP2P() {
    alert("Открытие P2P Маркета: здесь пользователи смогут размещать свои объявления об обмене.");
}

// Логика полета ракетки
let gameInterval;
function startRocket() {
    // Сброс позиций перед стартом
    clearInterval(gameInterval);
    const rocket = document.getElementById('rocket');
    const multiplierText = document.getElementById('multiplier');
    
    let currentMultiplier = 1.00;
    let posX = 10;
    let posY = 10;

    rocket.style.transform = `translate(0px, 0px) rotate(0deg)`;

    // Случайный момент взрыва ракетки (от 1.1 до 5.0x)
    const crashPoint = (Math.random() * 4 + 1.1).toFixed(2);

    gameInterval = setInterval(() => {
        currentMultiplier += 0.02;
        multiplierText.innerText = currentMultiplier.toFixed(2) + 'x';

        // Движение ракетки по диагонали вверх
        if (posX < 220) posX += 1.5;
        if (posY < 100) posY += 1.0;
        
        rocket.style.bottom = `${10 + posY}px`;
        rocket.style.left = `${10 + posX}px`;
        rocket.style.transform = `rotate(-15deg)`; // Наклон при полете

        // Проверка на краш (взрыв)
        if (currentMultiplier >= crashPoint) {
            clearInterval(gameInterval);
            multiplierText.style.color = '#e74c3c';
            multiplierText.innerText = `ВЗРЫВ: ${currentMultiplier.toFixed(2)}x`;
            rocket.style.transform = `scale(0) rotate(0deg)`; // Исчезновение
            
            // Возврат в исходное состояние через 2 секунды
            setTimeout(() => {
                multiplierText.style.color = '#2ecc71';
                multiplierText.innerText = '1.00x';
                rocket.style.bottom = '10px';
                rocket.style.left = '10px';
                rocket.style.transform = `scale(1) rotate(0deg)`;
            }, 2000);
        }
    }, 50);
}
