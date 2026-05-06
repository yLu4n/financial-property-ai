import { useState } from "react";

function FinancialForm({ onSubmit, loading }){
    const [formData, setFormData] = useState({
        salario_bruto: 9000,
        outras_rendas: 0,
        despesas_fixas: 3000,
        despesas_variaveis: 1500,
        reserva_emergencia: 30000,
        dividas_atuais: 2000,
        property_value: 500000,
        monthly_rent: 2500
    });

    const handleChange = (e) => {
        setFormData({
            ...formData,
            [e.target.name]: Number(e.target.value)
        });
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        const payload = {
            financial_data: {
                salario_bruto: formData.salario_bruto,
                outras_rendas: formData.outras_rendas,
                despesas_fixas: formData.despesas_fixas,
                despesas_variaveis: formData.despesas_variaveis,
                reserva_emergencia: formData.reserva_emergencia,
                dividas_atuais: formData.dividas_atuais
            },
            property_value: formData.property_value,
            monthly_rent: formData.monthly_rent
        };

        onSubmit(payload);
    };

    return (
        <form onSubmit={handleSubmit}>
            {Object.keys(formData).map((key) => (
                <div key={key} style={{ marginBottom: "10px" }}>
                    <label>{key}</label>
                    <input type="number" name={key} value={formData[key]} onChange={handleChange} style={{ marginLeft: "10px" }} />
                </div>
            ))}

            <button type="submit">
                {loading ? "Analyzing..." : "Analyze"}
            </button>
        </form>
    )
}

export default FinancialForm