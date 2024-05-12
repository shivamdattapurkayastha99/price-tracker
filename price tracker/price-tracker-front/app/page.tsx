import Image from "next/image";
import React from "react";

import { AxisOptions, Chart } from "react-charts";
export default function Home() {
  type DailyStars = {
    date: Date,
    stars: number,
  }
  
  type Series = {
    label: string,
    data: DailyStars[]
  }
  
  const data: Series[] = [
    {
      label: 'React Charts',
      data: [
        {
          date: new Date(),
          stars: 202123,
        }
        // ...
      ]
    },
    {
      label: 'React Query',
      data: [
        {
          date: new Date(),
          stars: 10234230,
        }
        // ...
      ]
    }
  ]
  const primaryAxis = React.useMemo(
    (): AxisOptions<DailyStars> => ({
      getValue: datum => datum.date,
    }),
    []
  )

  const secondaryAxes = React.useMemo(
    (): AxisOptions<DailyStars>[] => [
      {
        getValue: datum => datum.stars,
      },
    ],
    []
  )
  return (
    <>
    <h1>Welcome to price tracker </h1>
    <div>
       <Chart
       options={{
         data,
         primaryAxis,
         secondaryAxes,
       }}
     />
    </div>
    </>
  );
}
