import axios from "axios";

const api = axios.create({
    baseURL: "http://127.0.0.1:8000",
});

export const runAnalysis = async (payload) => {
    const response = await api.post("/analysis", payload);
    return response.data.data;
}