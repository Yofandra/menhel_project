'use strict';

(function () {
  let cardColor, headingColor, labelColor, borderColor, legendColor;

  if (isDarkStyle) {
    cardColor = config.colors_dark.cardColor;
    headingColor = config.colors_dark.headingColor;
    labelColor = config.colors_dark.textMuted;
    legendColor = config.colors_dark.bodyColor;
    borderColor = config.colors_dark.borderColor;
  } else {
    cardColor = config.colors.cardColor;
    headingColor = config.colors.headingColor;
    labelColor = config.colors.textMuted;
    legendColor = config.colors.bodyColor;
    borderColor = config.colors.borderColor;
  }

  const lineChartEl = document.querySelector('#lineChart'),
    lineChartConfig = {
      chart: {
        height: 400,
        type: 'line',
        parentHeightOffset: 0,
        zoom: {
          enabled: false
        },
        toolbar: {
          show: false
        }
      },
      series: [
        {
          name: 'Garis',
          type: 'line',
          data: [280, 200, 220, 180, 270, 250, 70, 90, 200, 150, 160, 100]
        },
        {
          name: 'Batang',
          type: 'line',
          data: [20, 100, 120, 140, 170, 150, 50, 80, 180, 140, 120, 110]
        }
      ],
      markers: {
        strokeWidth: 7,
        strokeOpacity: 1,
        strokeColors: [cardColor],
        colors: [config.colors.warning]
      },
      dataLabels: {
        enabled: false
      },
      stroke: {
        curve: 'straight'
      },
      colors: [config.colors.warning, config.colors.info], // Warna untuk garis dan batang
      grid: {
        borderColor: borderColor,
        xaxis: {
          lines: {
            show: true
          }
        },
        padding: {
          top: -20
        }
      },
      tooltip: {
        custom: function ({ series, seriesIndex, dataPointIndex, w }) {
          return '<div class="px-3 py-2">' + '<span>' + series[seriesIndex][dataPointIndex] + '%</span>' + '</div>';
        }
      },
      xaxis: {
        categories: [
          'Jun 2023', 'Jul 2023', 'Aug 2023', 'Sep 2023', 'Oct 2023', 'Nov 2023', 'Dec 2023',
          'Jan 2024', 'Feb 2024', 'Mar 2024', 'Apr 2024', 'May 2024'
        ],
        axisBorder: {
          show: false
        },
        axisTicks: {
          show: false
        },
        labels: {
          style: {
            colors: labelColor,
            fontSize: '13px'
          }
        }
      },
      yaxis: {
        labels: {
          style: {
            colors: labelColor,
            fontSize: '13px'
          }
        }
      }
    };

if (typeof lineChartEl !== undefined && lineChartEl !== null) {
    const lineChart = new ApexCharts(lineChartEl, lineChartConfig);
    lineChart.render();
}
})();

