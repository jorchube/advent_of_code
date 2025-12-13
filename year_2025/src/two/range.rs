use super::id::Id;

#[derive(Debug, Clone)]
pub struct Range {
    start: u64,
    end: u64,
}

impl Range {
    pub fn new(start: u64, end: u64) -> Self {
        Range { start, end }
    }

    pub fn ids(&self) -> Vec<Id> {
        let raw_ids = (self.start..=self.end).collect::<Vec<u64>>();
        let ids = raw_ids
            .iter()
            .map(|raw_id| Id::new(raw_id.to_string()))
            .collect::<Vec<Id>>();

        ids
    }
}
