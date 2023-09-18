import { API_BASE_URL } from "./config";
import axios from "axios";

const axiosInstance = axios.create({
    baseURL: API_BASE_URL
})

export const dogFactsService = {
    getFact: async () => {
        return await axiosInstance.get("/dog_fact")
            .then((response) => response)
            .catch((error) => error);
    }
}