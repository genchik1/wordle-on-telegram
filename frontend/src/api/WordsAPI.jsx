import axios from "axios";
import {apiDomain, tgUser} from "../Constants.jsx";

export async function getTodayWord() {
    let link = `${apiDomain}/api/words/today`;
    const response = await axios.get(link);
    return response.data;
}

export async function checkWord(word) {
    let link = `${apiDomain}/api/words/check`;
    const response = await axios.get(link, {params: {word: word, user_id: tgUser}});
    return response.data;
}

export async function getUserWords() {
    let link = `${apiDomain}/api/words/user`;
    const response = await axios.get(link, {params: {user_id: tgUser}});
    return response.data;
}
