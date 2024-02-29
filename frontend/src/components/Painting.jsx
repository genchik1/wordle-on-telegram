import {cssVar} from "../utils.js";
import {checkWord} from "../api/WordsAPI.jsx";

export const handleClick = (dataKey, state, line, setState, keyColor, rightWord, setLine) => {
    let tg = window.Telegram.WebApp;
    document.getElementById('button_enter').style.backgroundColor = cssVar("--button-color");
    document.getElementById('button_enter').style.color = cssVar("--button-text-color");
    document.getElementById('button_enter').style.width = "58px";
    document.getElementById('button_backspace').style.backgroundColor = cssVar("--button-color");
    document.getElementById('button_backspace').style.color = cssVar("--button-text-color");

    let newTextColor = keyColor;

    if (tg.colorScheme === "dark") {
        newTextColor = '#212121';
    }

    switch (dataKey) {
        case 'backspace': {
            if (state[line].length > 0) {
                const newState = state[line].slice(0, -1);
                setState({...state, [line]: newState});
            }
            for (let i = 0; i < 5; i++) {
                let itemStyle = document.getElementById(`item_${line}_${i + 1}`).style;
                itemStyle.color = cssVar("--text-color");
                itemStyle.backgroundColor = keyColor;
            }
            break;
        }
        case 'enter': {
            if (state[line].length < 5) {
                console.log('Недостаточно букв');
            } else {
                const userWord = state[line];

                checkWord(userWord.join('')).then(
                    isTrueWord => {
                        let correctLetters = 0;
                        for (let i = 0; i < userWord.length; i++) {
                            let itemStyle = document.getElementById(`item_${line}_${i + 1}`).style;
                            let buttonStyle = document.getElementById(`button_${userWord[i]}`).style;
                            // Закрашиваем в красный цвет если такого слова не существует в базе
                            if (!isTrueWord) {
                                itemStyle.color = newTextColor;
                                itemStyle.backgroundColor = 'red';
                            } else {
                                for (let j = 0; j < userWord.length; j++) {
                                    // Закрашиваем в желтый цвет буквы которые пристуствуют в слове
                                    if (userWord[i] === rightWord[j]) {
                                        if (itemStyle.backgroundColor !== 'green') {
                                            itemStyle.backgroundColor = '#FFB74D';
                                        }
                                        if (buttonStyle.backgroundColor !== 'green') {
                                            buttonStyle.backgroundColor = '#FFB74D';
                                        }
                                        itemStyle.color = newTextColor;
                                        buttonStyle.color = newTextColor;
                                    } else {
                                        // Закрашиваем в серый цвет
                                        if (itemStyle.backgroundColor !== 'green' && itemStyle.backgroundColor !== '#FFB74D') {
                                            itemStyle.backgroundColor = '#90A4AE';
                                        }
                                        if (buttonStyle.backgroundColor !== 'green' && buttonStyle.backgroundColor !== '#FFB74D') {
                                            buttonStyle.backgroundColor = '#90A4AE';
                                        }
                                    }

                                }
                                // Закрашиваем в зеленый цвет совпадающие буквы
                                if (userWord[i] === rightWord[i]) {
                                    if (itemStyle.backgroundColor !== 'red') {
                                        itemStyle.backgroundColor = 'green';
                                    }
                                    itemStyle.color = newTextColor;
                                    buttonStyle.backgroundColor = 'green';
                                    buttonStyle.color = newTextColor;
                                    correctLetters = correctLetters + 1
                                }
                            }
                        }
                        if (!isTrueWord) {
                            tg.HapticFeedback.notificationOccurred("error");
                        } else if (correctLetters === 5) {
                            tg.HapticFeedback.notificationOccurred("success");
                            setLine(1);
                            return navigate('/success')
                        } else {
                            tg.HapticFeedback.notificationOccurred("error");
                            setLine(line + 1);
                        }
                    });
            }
            break;
        }
        default: {
            if (state[line].length < 5) {
                setState({...state, [line]: [...state[line], dataKey]});
            }
            break;
        }
    }
};