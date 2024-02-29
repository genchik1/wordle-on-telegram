import {Box, CardContent, CardMedia, Typography} from "@mui/material";
import {useState} from "react";
import {cssVar} from "../utils.js";

const generateRandomNumber = () => {
    const min = 1;
    const max = 5;
    return Math.floor(Math.random() * (max - min + 1)) + min;
};


export function Success() {
    let tg = window.Telegram.WebApp;
    if (tg.colorScheme === "light") {
        tg.setHeaderColor(cssVar("--button-color"));
    }
    // tg.BackButton.show();
    // const navigate = useNavigate();
    // tg.BackButton.onClick(() => navigate("/"));

    const [randomNumber, setRandomNumber] = useState(generateRandomNumber());

    return <Box>
        <CardContent sx={{color: cssVar("--text-color")}}>
            <Typography variant='h6'>🎉 Ура! Вы угадали слово!</Typography>
            <Typography variant='caption'>Новое слово в 9 утра по мск.</Typography>
        </CardContent>
        <CardMedia sx={{borderRadius: "10px", maxHeight: "500px"}} component="img" image={`./${randomNumber}.gif`} alt="img"/>
    </Box>
}
