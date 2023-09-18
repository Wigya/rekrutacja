import { API_BASE_URL } from "./config";
import axios from "axios";

const axiosInstance = axios.create({
    baseURL: API_BASE_URL
})

export const favoriteService = {
    getFavorites: async () => {
        return await axiosInstance.get("/favorite")
            .then((response) => response)
            .catch((error) => error);
    },
    addFavorite: async (data: { "data": string }) => {
        return await axiosInstance.post("favorite", data)
            .then(response => response)
            .catch((error) => error);
    },
    deleteFavorite: async (text: string) => {
        return await axiosInstance.delete(`/favorite/${text}`)
            .then((response) => response)
            .catch((error) => error);
    },
    updateFavorite: async (body: { "original": string, "newValue": string }) => {
        return await axiosInstance.patch("/favorite", body)
            .then((response) => response)
            .catch((error) => error);
    }
}