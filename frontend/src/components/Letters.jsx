import {cssVar} from "../utils.js";
import {Box, Button, Grid, Typography} from "@mui/material";
import {useState} from "react";
import {keys} from "../data/keys.js";


function BoxKey({id, backgroundColor, textColor, child}) {
    return <Box id={id} sx={{
        backgroundColor: backgroundColor,
        textAlign: 'center',
        color: textColor,
        borderRadius: "5px",
        height: "46px",
        width: "46px",
        fontSize: 20,
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
    // document.getElementById('button_enter').style.backgroundColor = cssVar("--button-color");
    // document.getElementById('button_enter').style.color = cssVar("--button-text-color");
    // document.getElementById('button_enter').style.width = "58px";
    // document.getElementById('button_backspace').style.backgroundColor = cssVar("--button-color");
    // document.getElementById('button_backspace').style.color = cssVar("--button-text-color");

    let keyColor = cssVar("--bg-color");
    let keyTextColor = cssVar("--text-color");
    const [line, setLine] = useState(1)
    const [state, setState] = useState({
        1: [],
        2: [],
        3: [],
        4: [],
        5: [],
        6: [],
    });

    const handleClick = (dataKey) => {
        switch (dataKey) {
            case 'backspace': {
                if (state[line].length > 0) {
                    const newState = state[line].slice(0, -1);
                    setState({...state, [line]: newState});
                }
                break;
            }
            case 'enter': {
                if (state[line].length < 5) {
                    console.log('Недостаточно букв');
                } else {
                    const userWord = state[line];
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
                        }
                        if (userWord[i] === rightWord[i]) {
                            let itemStyle = document.getElementById(`item_${line}_${i + 1}`).style;
                            let buttonStyle = document.getElementById(`button_${userWord[i]}`).style;
                            itemStyle.backgroundColor = 'green';
                            itemStyle.color = '#fff';
                            buttonStyle.backgroundColor = 'green';
                            buttonStyle.color = '#fff';
                            correctLetters = correctLetters + 1
                        }
                    }
                    if (correctLetters === 5) {
                        setLine(1);
                    } else {
                        setLine(line + 1);
                    }
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
    let style={textAlign: "center", justifyContent: "center", alignItems: "center"}
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
                padding: "0px"
            }}>
                <Grid container spacing={1}>
                    {keys.map((item) => (
                        <Grid item xs={1} sm={2} md={2} key={item.id}>
                            <Button
                                id={`button_${item.attribute}`}
                                key={item.id}
                                sx={{
                                    backgroundColor: keyColor, color: keyTextColor,
                                    height: "30px", minWidth: "24px", fontSize: 9,
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