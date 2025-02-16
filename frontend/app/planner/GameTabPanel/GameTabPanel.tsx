import { Box } from '@mui/material';

export interface GameTabPanelProps {
  children?: React.ReactNode;
  index: number;
  value: number;
}

export const GameTabPanel = (props: GameTabPanelProps) => {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`tabpanel-${index}`}
      aria-labelledby={`tab-${index}`}
      {...other}
    >
      {value === index && (
        children
      )}
    </div>
  );
};