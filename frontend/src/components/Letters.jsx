import {cssVar} from "../utils.js";
import {Box, Button, Grid, Typography} from "@mui/material";
import {useState} from "react";
import {keys} from "../data/keys.js";
import {checkWord, getUserWords} from "../api/WordsAPI.jsx";
import {useNavigate} from "react-router-dom";


function BoxKey({id, backgroundColor, textColor, child}) {
    return <Box id={id} sx={{
        backgroundColor: backgroundColor,
        textAlign: 'center',
        color: textColor,
        borderRadius: "5px",
        height: "46px",
        width: "46px",
        fontSize: 20,
        borderColor: cssVar('--button-color'),
    }}>
        <Typography
            variant='h6'
            sx={{textTransform: 'uppercase', textAlign: 'center', paddingTop: "8px"}}
        >
            {child}
        </Typography>
    </Box>
}


function FormRow({backgroundColor, textColor, state, line}) {
    return (
        <>
            <Grid item xs={1} sm={2} md={2}>
                <BoxKey id={`item_${line}_${1}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[0]
                }/>
            </Grid>
            <Grid item xs={1} sm={2} md={2}>
                <BoxKey id={`item_${line}_${2}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[1]
                }/>
            </Grid>
            <Grid item xs={1} sm={2} md={2}>
                <BoxKey id={`item_${line}_${3}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[2]
                }/>
            </Grid>
            <Grid item xs={1} sm={1} md={2}>
                <BoxKey id={`item_${line}_${4}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[3]
                }/>
            </Grid>
            <Grid item xs={1} sm={1} md={2}>
                <BoxKey id={`item_${line}_${5}`} backgroundColor={backgroundColor} textColor={textColor} child={
                    state[4]
                }/>
            </Grid>
        </>
    );
}


export function Letters({rightWord}) {
    let tg = window.Telegram.WebApp;
    const navigate = useNavigate();
    let keyColor = cssVar("--bg-color");
    let keyTextColor = cssVar("--text-color");
    const [line, setLine] = useState(1)
    const [isGet, setIsGet] = useState(false);
    const [state, setState] = useState({
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    });

    if (!isGet) {
        getUserWords().then(result => {
            setState(result.words);
            setIsGet(true);
            if (result.is_guessed) {
                return navigate('/success');
            }
            for (let i = 1; i < 7; i++) {
                console.log(result.words[i], result.words[i].length);
                if (result.words[i].length === 0) {
                    setLine(i);
                    break;
                }
            }
        });
    }

    const handleClick = (dataKey) => {
        document.getElementById('button_enter').style.backgroundColor = cssVar("--button-color");
        document.getElementById('button_enter').style.color = cssVar("--button-text-color");
        document.getElementById('button_enter').style.width = "58px";
        document.getElementById('button_backspace').style.backgroundColor = cssVar("--button-color");
        document.getElementById('button_backspace').style.color = cssVar("--button-text-color");

        switch (dataKey) {
            case 'backspace': {
                if (state[line].length > 0) {
                    const newState = state[line].slice(0, -1);
                    setState({...state, [line]: newState});
                }
                for (let i = 0; i < 5; i++) {
                    let itemStyle = document.getElementById(`item_${line}_${i + 1}`).style;
                    itemStyle.color = '#fff';
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
                                for (let j = 0; j < userWord.length; j++) {
                                    if (userWord[i] === rightWord[j]) {
                                        let itemStyle = document.getElementById(`item_${line}_${i + 1}`).style;
                                        let buttonStyle = document.getElementById(`button_${userWord[i]}`).style;

                                        if (itemStyle.backgroundColor !== 'green') {
                                            itemStyle.backgroundColor = '#FFB74D';
                                        }
                                        if (buttonStyle.backgroundColor !== 'green') {
                                            buttonStyle.backgroundColor = '#FFB74D';
                                        }
                                        itemStyle.color = '#fff';
                                        buttonStyle.color = '#fff';
                                    }
                                    if (!isTrueWord) {
                                        let itemStyle = document.getElementById(`item_${line}_${i + 1}`).style;
                                        itemStyle.color = '#fff';
                                        itemStyle.backgroundColor = 'red';
                                    }
                                }
                                if (userWord[i] === rightWord[i]) {
                                    let itemStyle = document.getElementById(`item_${line}_${i + 1}`).style;
                                    let buttonStyle = document.getElementById(`button_${userWord[i]}`).style;
                                    if (itemStyle.backgroundColor !== 'red') {
                                        itemStyle.backgroundColor = 'green';
                                    }
                                    itemStyle.color = '#fff';
                                    buttonStyle.backgroundColor = 'green';
                                    buttonStyle.color = '#fff';
                                    correctLetters = correctLetters + 1
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
    let style = {textAlign: "center", justifyContent: "center", alignItems: "center"}
    return (
        <Grid sx={{flexGrow: 1}} container>
            <Grid container spacing={1} justifyContent="center" sx={{marginLeft: "-30px"}}>
                <Grid container item spacing={7} sx={style}>
                    <FormRow line={1}
                             backgroundColor={keyColor}
                             textColor={keyTextColor}
                             positionLine={1}
                             state={state[1]}/>
                </Grid>
                <Grid container item spacing={7} sx={style}>
                    <FormRow line={2}
                             backgroundColor={keyColor}
                             textColor={keyTextColor}
                             positionLine={2}
                             state={state[2]}/>
                </Grid>
                <Grid container item spacing={7} sx={style}>
                    <FormRow line={3}
                             backgroundColor={keyColor}
                             textColor={keyTextColor}
                             positionLine={3}
                             state={state[3]}/>
                </Grid>
                <Grid container item spacing={7} sx={style}>
                    <FormRow line={4}
                             backgroundColor={keyColor}
                             textColor={keyTextColor}
                             positionLine={4}
                             state={state[4]}/>
                </Grid>
                <Grid container item spacing={7} sx={style}>
                    <FormRow line={5}
                             backgroundColor={keyColor}
                             textColor={keyTextColor}
                             positionLine={5}
                             state={state[5]}/>
                </Grid>
                <Grid container item spacing={7} sx={style}>
                    <FormRow line={6}
                             backgroundColor={keyColor}
                             textColor={keyTextColor}
                             positionLine={6}
                             state={state[6]}/>
                </Grid>
            </Grid>

            <Box sx={{
                position: "absolute",
                bottom: 70,
                marginLeft: "-12px",
                marginRight: "22px",
                padding: "0px",
            }}>
                <Grid container spacing={1}>
                    {keys.map((item) => (
                        <Grid item xs={1} sm={2} md={2} key={item.id}>
                            <Button
                                id={`button_${item.attribute}`}
                                key={item.id}
                                sx={{
                                    backgroundColor: keyColor, color: keyTextColor,
                                    height: "31px", minWidth: "26px", fontSize: 10,
                                    fontWeight: "bold"
                                }}
                                onClick={() => handleClick(item.attribute)}
                            >
                                {item.text}
                            </Button>
                        </Grid>
                    ))}
                </Grid>
            </Box>
        </Grid>
    )
}