import { RowItem } from '../readers/RowItem'
import { Analyser } from '../analysers/Analyser'
import { Reporter } from '../reporters/Reporter'

export class ReportGenerator {
  constructor(public analyser: Analyser<RowItem>, public reporter: Reporter) {}

  static printAnalysis() {
    // new Analyser<RowItem>()
  }
}
