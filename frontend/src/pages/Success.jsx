import {Box, CardContent, CardMedia, Typography} from "@mui/material";
import {useState} from "react";
import {useNavigate} from "react-router-dom";

const generateRandomNumber = () => {
    const min = 1;
    const max = 5;
    return Math.floor(Math.random() * (max - min + 1)) + min;
};


export function Success() {
    let tg = window.Telegram.WebApp;
    tg.BackButton.show();
    const navigate = useNavigate();
    tg.BackButton.onClick(() => navigate("/"));

    const [randomNumber, setRandomNumber] = useState(generateRandomNumber());

    return <Box>
        <CardContent>
            <Typography variant='h6'>🎉 Ура! Вы угадали слово!</Typography>
            <Typography variant='caption'>Новое слово в 9 утра по мск.</Typography>
        </CardContent>
        <CardMedia sx={{borderRadius: "10px", maxHeight: "500px"}} component="img" image={`/src/assets/${randomNumber}.gif`} alt="img"/>
    </Box>
}
