import {Box} from "@mui/material";
import {Letters} from "../components/Letters.jsx";
import {getTodayWord} from "../api/WordsAPI.jsx";
import {useQuery} from "@tanstack/react-query";
import {Title} from "../components/Title.jsx";
import {cssVar} from "../utils.js";
import axios from "axios";
import {apiDomain, tgUser} from "../Constants.jsx";

export function Game() {
    let tg = window.Telegram.WebApp;
    if (tg.colorScheme === "light") {
        tg.setHeaderColor(cssVar("--button-color"));
    }
    tg.BackButton.hide();
    tg.ready();
    tg.expand();

    let {isPending, isError, data, error} = useQuery({
        queryKey: ["word"],
        queryFn: () => getTodayWord(),
    });

    if (isError) {
        return <>Возникла ошибка</>
    }

    axios.post(apiDomain + `/api/user`, {
        id: tg.initDataUnsafe.user.id,
        username: tg.initDataUnsafe.user.username,
        allows_write_to_pm: tg.initDataUnsafe.user.allows_write_to_pm,
        utm: '',
    })

    return <Box>
        <Title/>
        {!isPending && <Letters rightWord={data}/>}
    </Box>
}
