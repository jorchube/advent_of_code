use super::id::Id;

#[derive(Debug, Clone)]
pub struct Range {
    start: u32,
    end: u32,
}

impl Range {
    pub fn new(start: u32, end: u32) -> Self {
        Range { start, end }
    }

    pub fn ids(&self) -> Vec<Id> {
        let raw_ids = (self.start..=self.end).collect::<Vec<u32>>();
        let ids = raw_ids
            .iter()
            .map(|raw_id| Id::new(raw_id.to_string()))
            .collect::<Vec<Id>>();

        ids
    }
}
