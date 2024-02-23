import {Box} from "@mui/material";
import {Letters} from "../components/Letters.jsx";
import {getTodayWord} from "../api/WordsAPI.jsx";
import {useQuery} from "@tanstack/react-query";
import {Title} from "../components/Title.jsx";

export function Game() {
    let { isPending, isError, data, error } = useQuery({
        queryKey: ["word"],
        queryFn: () => getTodayWord(),
    });

    if (isError) {
        return <>Возникла ошибка</>
    }

    return <Box >
        <Title />
        {!isPending && <Letters rightWord={data}/>}
    </Box>
}
