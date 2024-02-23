import {Box} from "@mui/material";
import {Letters} from "../components/Letters.jsx";
import {getTodayWord} from "../api/WordsAPI.jsx";
import {useQuery} from "@tanstack/react-query";
import {Title} from "../components/Title.jsx";
import {cssVar} from "../utils.js";

export function Game() {
    let tg = window.Telegram.WebApp;
    tg.setBackgroundColor('secondary_bg_color');
    if (tg.colorScheme === "light") {
        tg.setHeaderColor(cssVar("--button-color"));
    }
    tg.ready();
    tg.expand();

    let {isPending, isError, data, error} = useQuery({
        queryKey: ["word"],
        queryFn: () => getTodayWord(),
    });

    if (isError) {
        return <>Возникла ошибка</>
    }

    return <Box>
        <Title/>
        {!isPending && <Letters rightWord={data}/>}
    </Box>
}
