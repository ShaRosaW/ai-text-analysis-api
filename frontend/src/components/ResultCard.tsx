type Props = {
  title: string;
  children: React.ReactNode;
};

export function ResultCard({ title, children }: Props) {
  return (
    <div className="card">
      <h2>{title}</h2>
      {children}
    </div>
  );
}