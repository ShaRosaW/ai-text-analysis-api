import { useState } from "react";

type Props = {
  onSubmit: (text: string) => Promise<void>;
  loading: boolean;
};

export function TextForm({ onSubmit, loading }: Props) {
  const [text, setText] = useState("");

  const handleSubmit = async (
    e: React.SyntheticEvent<HTMLFormElement, SubmitEvent>
  ) => {
    e.preventDefault();
    await onSubmit(text);
  };

  return (
    <form onSubmit={handleSubmit} className="form">
      <label htmlFor="text">Input text</label>

      <textarea
        id="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Paste or type text here..."
        rows={10}
      />

      <button type="submit" disabled={loading || !text.trim()}>
        {loading ? "Analyzing..." : "Analyze"}
      </button>
    </form>
  );
}