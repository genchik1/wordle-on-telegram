import axios from "axios";
import {apiDomain, tgUser} from "../Constants.jsx";

export async function getTodayWord() {
    let link = `${apiDomain}/api/words/today`;
    const response = await axios.get(link, {
        params: {
            user_id: tgUser,
            //init_data:  window.Telegram.WebApp.initData,
        },
    });
    return response.data;
}
