import React from 'react';
import clsx from 'clsx';
import styles from './styles.module.css';

const FeatureList = [
  {
    Svg: require('@site/static/img/code_demo.svg').default,
  },
];

function Feature({Svg, title, description}) {
  return (
    <div className={clsx('col col--12')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
    </div>
  );
}

export default function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
