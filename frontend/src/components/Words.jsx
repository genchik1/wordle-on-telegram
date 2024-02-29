import {cssVar} from "../utils.js";
import {Box, Button, Grid, Typography} from "@mui/material";
import {useState} from "react";
import {keys} from "../data/keys.js";
import {getUserWords} from "../api/WordsAPI.jsx";
import {useNavigate} from "react-router-dom";
import {FormRow} from "./Row.jsx";
import {handleClick} from "./Painting.jsx";


export function Words({rightWord}) {
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


    let style = {textAlign: "center", justifyContent: "center", alignItems: "center"}
    return (
        <Grid sx={{flexGrow: 1}} container>
            <Grid container spacing={1} justifyContent="center" sx={{marginLeft: "-30px"}}>
                {
                    [1, 2, 3, 4, 5, 6].map(line => (<Grid container item spacing={7} sx={style}>
                            <FormRow line={line}
                                     backgroundColor={keyColor}
                                     textColor={keyTextColor}
                                     positionLine={line}
                                     state={state[line]}/>
                        </Grid>)
                    )
                }
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
                                onClick={() => handleClick(item.attribute, state, line, setState, keyColor, rightWord, setLine)}
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