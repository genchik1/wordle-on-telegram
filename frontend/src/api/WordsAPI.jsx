import axios from "axios";
import {apiDomain} from "../Constants.jsx";

export async function getTodayWord() {
    let link = `${apiDomain}/api/words/today`;
    const response = await axios.get(link);
    return response.data;
}
