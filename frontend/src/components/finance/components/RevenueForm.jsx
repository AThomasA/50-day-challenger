import { useState } from "react";
import { Button } from "../../ui/Button";
import { Input } from "../../ui/Input";

export function RevenueForm({ onSubmit }) {
  const [description, setDescription] = useState("");
  const [amount, setAmount] = useState("");
  const [date, setDate] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!description || !amount || !date) return;

    await onSubmit({
      description,
      amount: Number(amount),
      date,
    });

    // limpa o formulário
    setDescription("");
    setAmount("");
    setDate("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <Input
        placeholder="Descrição"
        value={description}
        onChange={(e) => setDescription(e.target.value)}
      />

      <Input
        type="number"
        placeholder="Valor"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />

      <Input
        type="date"
        value={date}
        onChange={(e) => setDate(e.target.value)}
      />

      <Button type="submit">Adicionar Receita</Button>
    </form>
  );
}
